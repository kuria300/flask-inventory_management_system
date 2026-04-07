from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
from file_reader import load_db, save_db
from models import Product

load_dotenv()
from config import Config

app=Flask(__name__)
app.config.from_object(Config)


def get_food_facts(barcode):
    """Get product by barcode """
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}.json"

    
    response=requests.get(url, 
        headers={"User-Agent": "MyInventoryApp/1.0"},
        auth=("off", "off")
    )

    if response.status_code == 200:
        data=response.json()
        if data.get('status') == 1:

            return data.get('product')
    return None

# get all
@app.route('/inventory', methods=['GET'])
def get_all():
    products = load_db()

    return jsonify(products), 200
# get one by barcode
@app.route('/inventory/<string:barcode>', methods=['GET'])
def get_one(barcode):
    products=load_db()

    one_product= next((p for p in products if p.get('code') == barcode), None)

    if one_product:
        return jsonify(one_product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/inventory', methods=['POST'])
def add_one_barcode():
    data = request.get_json()
    code = data.get("code")

    if not code:
        return jsonify({"error": "missing barcode"}), 400

    # check if its in our db
    product_list=load_db()
    if next((p for p in product_list if p.get('code') == code), None):
        return jsonify({"error": "product exists in database"}), 400


    # fetch from api
    api_product=get_food_facts(code)
    if not api_product:
        return jsonify({"error": "Product not found, check code"}), 404

    if product_list:
        new_id= max(p.get('id', 0) for p in product_list) + 1
    else:
        new_id=1

    p1=Product(
        id=new_id,
        code=code,
        product_name=api_product.get('product_name', 'Unknown'),
        brand=api_product.get('brands', 'Unknown'),
        image=api_product.get('image_url', ''),
        nutriscore=api_product.get('nutriscore_grade', 'unknown')
    )

    product_list.append(p1.__dict__)
    save_db(product_list)

    return jsonify(p1.__dict__), 201

@app.route('/inventory/<int:id>', methods=['PATCH'])
def patch_one(id):
    data=request.get_json()
    score=data.get('nutriscore')

    if not score:
        return jsonify({"error": "missing data for update"}), 400

    product_list=load_db()

    update_prod= next((p for p in product_list if p.get('id') == id), None)

    if not update_prod:
        return jsonify({"error": "Product not found"}), 404

    update_prod['nutriscore'] = score

    save_db(product_list)

    return jsonify(update_prod), 200

@app.route('/inventory/<int:id>', methods=['DELETE'])
def remove_one(id):

    product_list=load_db()

    new_list=[p for p in product_list if p.get('id') != id]

    if len(new_list) == len(product_list):
        return jsonify({"error":"Product not found, check ID"})

    save_db(new_list)

    return "",204















if __name__== "__main__":
    app.run()