from inventory.database import inventory
from unittest.mock import patch

#testing health endpoint
def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"

#testing inventory endpoint
def test_get_inventory(client):

    response = client.get("/inventory")

    assert response.status_code == 200

    assert isinstance(response.get_json(), list)

# trying to test getting an item that is not in the inventory
def test_get_missing_item(client):

    response = client.get("/inventory/999")

    assert response.status_code == 404

    assert response.get_json()["error"] == "Item not found"

# trying to test deleting an item that is not in the inventory
def test_delete_missing_item(client):

    response = client.delete("/inventory/999")

    assert response.status_code == 404

    assert response.get_json()["error"] == "Item not found"

    # Testing POST
    # testing adding an item to the inventory
@patch("inventory.services.fetch_product_by_barcode")
def test_add_item(mock_fetch, client):

    mock_fetch.return_value = {
        "barcode": "12345",
        "product_name": "Test Product",
        "brand": "Test Brand",
        "category": "Test Category",
        "ingredients": "Water"
    }

    payload = {
        "barcode": "12345",
        "price": 15.99,
        "stock": 20
    }

    response = client.post(
        "/inventory",
        json=payload
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["product_name"] == "Test Product"

    assert data["price"] == 15.99

    assert data["stock"] == 20

def test_add_item_invalid(client):

    payload = {
        "price": 10
    }

    response = client.post(
        "/inventory",
        json=payload
    )

    assert response.status_code == 400

    assert "error" in response.get_json()
 
 #testing duplicate barcode
@patch("inventory.services.fetch_product_by_barcode")
def test_duplicate_barcode(mock_fetch, client):

    # Mock OpenFoodFacts response
    mock_fetch.return_value = {
        "barcode": "12345",
        "product_name": "Milk",
        "brand": "Brand",
        "category": "Dairy",
        "ingredients": "Water"
    }

    # Existing inventory item
    inventory.append({
        "id": 1,
        "barcode": "12345",
        "product_name": "Milk",
        "brand": "Brand",
        "category": "Dairy",
        "ingredients": "Water",
        "price": 10,
        "stock": 5,
        "created_at": "2025-01-01",
        "updated_at": "2025-01-01"
    })

    payload = {
        "barcode": "12345",
        "price": 20,
        "stock": 15
    }

    response = client.post("/inventory", json=payload)

    assert response.status_code == 409

    assert response.get_json()["error"] == "Product already exists in inventory"

def test_patch_missing_item(client):

    response = client.patch(
        "/inventory/999",
        json={
            "price":20
        }
    )

    assert response.status_code == 404

def test_update_product(client):

    inventory.append({
        "id": 1,
        "barcode": "12345",
        "product_name": "Milk",
        "brand": "Brand",
        "category": "Dairy",
        "ingredients": "Water",
        "price": 10,
        "stock": 5,
        "created_at": "2025-01-01",
        "updated_at": "2025-01-01"
    })

    response = client.patch(
        "/inventory/1",
        json={
            "price": 50,
            "stock": 100
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["price"] == 50

    assert data["stock"] == 100


def test_update_missing_product(client):

    response = client.patch(
        "/inventory/999",
        json={
            "price": 50
        }
    )

    assert response.status_code == 404

    assert response.get_json()["error"] == "Item not found"


@patch("external.routes.fetch_product_by_barcode")
@patch("external.routes.map_product")
def test_search_product(mock_map, mock_fetch, client):

    mock_fetch.return_value = {"dummy": "data"}

    mock_map.return_value = {
        "barcode": "12345",
        "product_name": "Milk"
    }

    response = client.get("/products/barcode/12345")

    assert response.status_code == 200

    assert response.get_json()["product_name"] == "Milk"