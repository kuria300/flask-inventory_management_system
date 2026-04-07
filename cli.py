import requests

def show_menu():
    print("\n---Inventory Management System---")
    print("1. View All Items (GET)")
    print("2. Search Item by Barcode (GET)")
    print("3. Add New Item by Barcode (POST)")
    print("4. Update Data (PATCH)")
    print("5. Delete Item (DELETE)")
    print("6. Exit")

def get_products():
    res=requests.get('http://127.0.0.1:5000/inventory')
    data=res.json()
    
    if not data:
        print("\n The inventory is currently empty.")
        return

    for d in data:
        print(f"{d['code']} {d['product_name']} {d['brand']} - {d['nutriscore']} ")

def get_by_barcode():
    barcode = input("Enter Barcode: ")

    payload={"code": barcode}

    res=requests.get(F'http://127.0.0.1:5000/inventory/{barcode}')
    data=res.json()

    if res.status_code == 200:
        print(f"{data['code']} {data['product_name']} {data['brand']} - {data['nutriscore']} ")
    else:
        print(f'\n {data.get('error')}')


def add_by_barcode():
    barcode = input("Enter Barcode: ")

    res=requests.post('http://127.0.0.1:5000/inventory', json={'code': barcode})
    data=res.json()
    if res.status_code == 201:
        print("Product added successfully!")
    else:
        print(f"\n {data.get('error')}")

def patch_one():
    id=input("Enter id: ")

    data = {
    "nutriscore": "b"
    }

    res=requests.patch(f'http://127.0.0.1:5000/inventory/{id}', json=data)
    prod=res.json()

    if res.status_code == 200:
        print('Successfully patched product')
        print(prod)
    else:
        data=res.json()
        print(f"\n {data.get('error')}")

def delete_item():
    id=input('Enter id: ')

    res=requests.delete(f'http://127.0.0.1:5000/inventory/{id}')
    
    if res.status_code == 204:
        print('Successfully deleted data')
    else:
        data=res.json()
        print(f"\n {data.get('error')}")


if __name__== "__main__":
    while True:
        show_menu()
        option=input("Select an option: ")

        if option == "1":
            get_products()
        elif option == "2":
            get_by_barcode()
        elif option == "3":
            add_by_barcode()
        elif option == "4":
            patch_one()
        elif option == "5":
            delete_item()
        elif option == "6":
            print("Goodbye!")
            break
        
        else:
            print('Invalid Choice')
            continue

