# Inventory Management System

A Flask-based REST API and Command Line Interface (CLI) application for managing retail inventory with integration to the OpenFoodFacts API.

This project was developed as part of a Python REST API lab and demonstrates RESTful API design, external API integration, service-oriented architecture, and CLI application development.

---

## Features

### Inventory Management

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update inventory items
* Delete inventory items

### External API Integration

* Search products using their barcode
* Retrieve product information from the OpenFoodFacts API
* Automatically populate inventory records with product details

### Command Line Interface

* Interactive menu-driven interface
* View inventory
* View individual products
* Search products
* Add products
* Update products
* Delete products

---

## Technologies Used

* Python 3
* Flask
* Requests
* Rich
* OpenFoodFacts API

---

## Project Structure

```text
flask-inventory-management-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── cli/
│   ├── __init__.py
│   ├── api.py
│   ├── commands.py
│   ├── formatter.py
│   ├── main.py
│   ├── menu.py
│   └── theme.py
│
├── external/
│   ├── __init__.py
│   ├── openfoodfacts.py
│   └── routes.py
│
├── inventory/
│   ├── database.py
│   ├── routes.py
│   ├── services.py
│   ├── utils.py
│   └── validators.py
│
└── tests/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/mosweta-school/flask-inventory-management-system.git
```

Navigate into the project

```bash
cd flask-inventory-management-system
```

Create a virtual environment

Windows

```bash
python -m venv venv
```

Linux/macOS

```bash
python3 -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Flask API

Start the API server

```bash
python app.py
```

The API will be available at

```
http://127.0.0.1:5000
```

---

# Running the CLI

Open another terminal while the Flask server is running.

Run

```bash
python -m cli.main
```

The CLI communicates with the Flask API over HTTP.

---

# Testing
11 tests have been added. To carry out the test go to the project route.

Run

```bash
python3 -m pytest
```
# REST API Endpoints

## Health Check

| Method | Endpoint |
| ------ | -------- |
| GET    | /health  |

---

## Inventory

| Method | Endpoint        | Description                  |
| ------ | --------------- | ---------------------------- |
| GET    | /inventory      | Retrieve all inventory items |
| GET    | /inventory/<id> | Retrieve one inventory item  |
| POST   | /inventory      | Create inventory item        |
| PATCH  | /inventory/<id> | Update inventory item        |
| DELETE | /inventory/<id> | Delete inventory item        |

---

## External Product Search

| Method | Endpoint                    |
| ------ | --------------------------- |
| GET    | /products/barcode/<barcode> |

---

# Example POST Request

```json
{
    "barcode": "3017620422003",
    "price": 19.99,
    "stock": 50
}
```

Example Response

```json
{
    "id": 1,
    "barcode": "3017620422003",
    "product_name": "Nutella",
    "brand": "Ferrero",
    "category": "Confectionary based spreads",
    "ingredients": "...",
    "price": 19.99,
    "stock": 50,
    "created_at": "...",
    "updated_at": "..."
}
```

---

# Application Architecture

The application follows a layered architecture.

```
CLI
      │
      ▼
HTTP Requests
      │
      ▼
Flask Routes
      │
      ▼
Service Layer
      │
      ▼
Inventory Storage
```

This separation improves maintainability, readability, and scalability.

---

# OpenFoodFacts Integration

When adding a product, only the following information is supplied by the user:

* Barcode
* Price
* Stock

The application automatically retrieves additional product information from the OpenFoodFacts API including:

* Product Name
* Brand
* Category
* Ingredients

This minimizes manual data entry and improves inventory accuracy.

---

# Error Handling

The application validates:

* Missing barcode
* Missing price
* Missing stock
* Negative price
* Negative stock
* Duplicate products
* Invalid product barcode
* Product not found
* API connection errors

---

# Future Improvements

* Persistent database using SQLite or PostgreSQL
* User authentication
* Product images
* Barcode scanner support
* Inventory reports
* Docker deployment
* Automated unit tests
* Continuous Integration (GitHub Actions)

---

# Author
Deogracious Moriasi
