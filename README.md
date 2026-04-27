
# Inventory Management System

A complete inventory management system for a small retail company built with Python and Flask. This system provides a RESTful API for managing inventory items, integrates with the OpenFoodFacts API for product data, and includes a command-line interface for easy interaction.

## Features

- **RESTful API**: Full CRUD operations for inventory items using Flask
- **Database**: JSON file-based storage (products.json)
- **External API Integration**: Fetch product details from OpenFoodFacts
- **CLI Interface**: Command-line tools for API interaction

## Project Structure

```
inventory-management/
├── app.py                 # Main Flask application
├── models.py             # Product model
├── config.py             # Application configuration
├── cli.py                # Command-line interface (entrypoint)
├── file_reader.py        # JSON file operations
├── products.json         # Data storage file
├── Pipfile               # Pipenv dependencies
├── Pipfile.lock          # Pipenv lock file
└── README.md             # This file
```

## Prerequisites

- Python 3.10 or higher
- pipenv (for dependency management)

## Installation

1. **Clone or download the project files**
   ```bash
     git clone (https://github.com/username/repo.git)
   ```
2. **Install dependencies**
   ```bash
   pipenv install
   or
   pipenv sync (uses exact versions on pipfile.lock)
   ```

3. **Activate virtual environment**
   ```bash
   pipenv shell
   ```

4. **Use provided Config.py**

   Create a `.env` file in the project root or use provided Config.py and add to run in Debug mode:
   ```
   DEBUG=True
   ```

## Running the Application

### Start the Flask API Server

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000` by default.

### Using the Command-Line Interface

The CLI is the main entrypoint and interacts with the running Flask API. Make sure the server is running first then run in Split terminal.

```bash
python cli.py
```

## API Endpoints

### Inventory Items

- **GET /inventory** - Retrieve all inventory items
- **GET /inventory/<barcode>** - Retrieve a specific item by barcode
- **POST /inventory** - Create a new inventory item (provide barcode, it will fetches from OpenFoodFacts and create item)
- **PATCH /inventory/<id>** - Update an existing item (nutriscore field for tests)
- **DELETE /inventory/<id>** - Delete an item

### External API Integration

The system integrates with `OpenFoodFacts` API automatically when adding items by barcode.

## Database

The application uses JSON file-based storage in `products.json`. Data persists between application restarts.

### Product Model

Each inventory item in in-memory database, contains:
- `id`: Auto-generated unique identifier
- `code`: Barcode
- `product_name`: Product name (from OpenFoodFacts)
- `brand`: Brand information
- `image`: Product image URL
- `nutriscore`: Nutritional score

## Development

## Instructions to run application and interact with CLI and API for CRUD operations

### Using the CLI Interface

1. Start the Flask server in one terminal: `python app.py`
2. Open another terminal and run the CLI (Make sure venv is activated for step 1 and 2) : `python cli.py`
3. The CLI will display a menu with the following options:
   - **1. View All Items (GET)**: Displays all inventory items stored in products.json
   - **2. Search Item by Barcode (GET)**: Search for a specific item by entering its barcode
   - **3. Add New Item by Barcode (POST)**: Add a new item by providing a barcode (fetches details from OpenFoodFacts API)
   - **4. Update Data (PATCH)**: Update an existing item's nutriscore by providing the item ID
   - **5. Delete Item (DELETE)**: Remove an item from inventory by providing the item ID
   - **6. Exit**: Quit the CLI application

The CLI communicates with the running Flask API server to perform these operations just choose 1,2,3,4,5,6 where necessary input data e.g: Enter barcode- 3017624010701

4. The system will fetch product details from OpenFoodFacts and add to inventory

### Fetching Items endpoints example:

- GET `http://127.0.0.1:5000/inventory` - Get all items
- GET `http://127.0.0.1:5000/inventory/3017620422003` - Get item by barcode

## Dependencies

Managed via Pipenv:
- flask
- requests
- python-dotenv

## Contributors
   
Eugene Kuria Maina

## Contributing

Contributions are always welcome!

Please adhere to this project's `code of conduct`.

## License

This project is open source and available under the MIT License.

