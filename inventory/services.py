from external.openfoodfacts import (
    fetch_product_by_barcode,
    map_product,
)

from inventory.database import inventory
from inventory.utils import (
    current_timestamp,
    generate_inventory_id,
)
from inventory.validators import validate_inventory_data


def get_all_items():
    """Return all inventory items."""
    return inventory

def barcode_exists(barcode):
    return any(item["barcode"] == barcode for item in inventory)

def get_item(item_id):
    """Return an inventory item by its ID."""
    return next(
        (item for item in inventory if item["id"] == item_id),
        None,
    )




def add_item(data):
    """Create a new inventory item using OpenFoodFacts data."""
    # Validate request
    error = validate_inventory_data(data)
    if error:
        return {"error": error}, 400

    barcode = data["barcode"]
    price = data["price"]
    stock = data["stock"]

    # Prevent duplicates
    if barcode_exists(barcode):
        return {"error": "Product already exists in inventory"}, 409

    # Fetch product from OpenFoodFacts
    product = fetch_product_by_barcode(barcode)
    if product is None:
        return {"error": "Product not found"}, 404

    # Convert API response into our format
    product_data = map_product(product)

    # Build inventory item
    new_item = build_inventory_item(
        product_data=product_data,
        price=price,
        stock=stock,
    )

    # Save item
    inventory.append(new_item)

    return new_item, 201

def update_item(item_id, data):
    """Update an inventory item's stock and/or price."""

    item = get_item(item_id)

    if item is None:
        return None

    if "price" in data:
        if data["price"] < 0:
            return {"error": "Price must be zero or greater"}, 400
        item["price"] = data["price"]

    if "stock" in data:
        if data["stock"] < 0:
            return {"error": "Stock must be zero or greater"}, 400
        item["stock"] = data["stock"]

    item["updated_at"] = current_timestamp()

    return item

def delete_item(item_id):

    item = get_item(item_id)

    if item is None:
        return False

    inventory.remove(item)

    return True




def build_inventory_item(product_data, price, stock):
    """
    Build a complete inventory item from product and inventory data.
    """
    timestamp = current_timestamp()

    return {
        "id": generate_inventory_id(inventory),
        **product_data,
        "price": price,
        "stock": stock,
        "created_at": timestamp,
        "updated_at": timestamp,
    }