import requests
from config import OPENFOODFACTS_API



HEADERS = {
    "User-Agent": "FlaskInventoryManagementSystem/1.0 (student project)"
}

def fetch_product_by_barcode(barcode):
    url = f"{OPENFOODFACTS_API}/{barcode}.json"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    print(response.status_code)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    return data["product"]

def map_product(product):
    brand = product.get("brands", "").split(",")[0].strip()

    category = (
        product.get("categories_en")
        or product.get("categories")
        or ""
    ).split(",")[0].replace("en:", "").strip()

    return {
        "barcode": product.get("code", ""),
        "product_name": (
            product.get("product_name_en")
            or product.get("product_name")
            or "Unknown Product"
        ),
        "brand": brand if brand else "Unknown Brand",
        "category": category if category else "Unknown Category",
        "ingredients": (
            product.get("ingredients_text_en")
            or product.get("ingredients_text")
            or "Not Available"
        )
    }