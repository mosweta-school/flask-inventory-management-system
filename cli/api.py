import requests
'''This file talks to flask'''
BASE_URL = "http://127.0.0.1:5000"


def get_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    return response.json()

def get_item(item_id):
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    return response.json()

def add_item(barcode, price, stock):
    payload = {
        "barcode": barcode,
        "price": price,
        "stock": stock,
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload,
    )

    return response.json()

def update_item(item_id, price, stock):
    payload = {
        "price": price,
        "stock": stock,
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload,
    )

    return response.json()

def delete_item(item_id):
    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    return response.json()

def search_product(barcode):
    '''search openfoodfacts'''
    response = requests.get(
        f"{BASE_URL}/products/barcode/{barcode}"
    )

    return response.json()