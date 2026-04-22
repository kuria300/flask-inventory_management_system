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

- Python 3.8 or higher
- pipenv (for dependency management)

## Installation

1. **Clone or download the project files**

2. **Install dependencies**
   ```bash
   pipenv install
   pipenv sync
   ```

3. **Activate virtual environment**
   ```bash
   pipenv shell
   ```

4. **Set up environment variables** (optional)
   Create a `.env` file in the project root or use provided Config.py:
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

The CLI is the main entrypoint and interacts with the running Flask API. Make sure the server is running first.

```bash
python cli.py
```

## API Endpoints

### Inventory Items

- **GET /inventory** - Retrieve all inventory items
- **GET /inventory/<barcode>** - Retrieve a specific item by barcode
- **POST /inventory** - Create a new inventory item (provide barcode, fetches from OpenFoodFacts)
- **PATCH /inventory/<id>** - Update an existing item (nutriscore field)
- **DELETE /inventory/<id>** - Delete an item

### External API Integration

The system integrates with OpenFoodFacts API automatically when adding items by barcode.

## Database

The application uses JSON file-based storage in `products.json`. Data persists between application restarts.

### Product Model

Each inventory item contains:
- `id`: Auto-generated unique identifier
- `code`: Barcode
- `product_name`: Product name (from OpenFoodFacts)
- `brand`: Brand information
- `image`: Product image URL
- `nutriscore`: Nutritional score

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 201: Created
- 204: No Content (for deletions)
- 400: Bad Request (validation errors)
- 404: Not Found
- 500: Internal Server Error

## Development

### Running in Debug Mode

Set `DEBUG=True` in your `.env` file or environment variables to enable debug mode.

## Usage Examples

### Using the CLI Interface

1. Start the Flask server in one terminal: `python app.py`
2. Open another terminal and run the CLI: `python cli.py`
3. The CLI will display a menu with the following options:
   - **1. View All Items (GET)**: Displays all inventory items stored in products.json
   - **2. Search Item by Barcode (GET)**: Search for a specific item by entering its barcode
   - **3. Add New Item by Barcode (POST)**: Add a new item by providing a barcode (fetches details from OpenFoodFacts API)
   - **4. Update Data (PATCH)**: Update an existing item's nutriscore by providing the item ID
   - **5. Delete Item (DELETE)**: Remove an item from inventory by providing the item ID
   - **6. Exit**: Quit the CLI application

The CLI communicates with the running Flask API server to perform these operations just choose 1,2,3,4,5,6 where necessary input data e.g: barcode- 3017624010701
4. The system will fetch product details from OpenFoodFacts and add to inventory

### Fetching Items endpoints example

- GET `http://127.0.0.1:5000/inventory` - Get all items
- GET `http://127.0.0.1:5000/inventory/3017620422003` - Get item by barcode

## Dependencies

Managed via Pipenv:
- flask
- requests
- python-dotenv

## License

This project is open source and available under the MIT License.