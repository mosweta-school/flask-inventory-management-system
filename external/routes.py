from flask import Blueprint, jsonify

from external.openfoodfacts import (
    fetch_product_by_barcode,
    map_product,
)

external_bp = Blueprint("external", __name__)


@external_bp.route("/products/barcode/<barcode>", methods=["GET"])
def search_product(barcode):
    """
    Search for a product by barcode using the OpenFoodFacts API.
    """

    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(map_product(product)), 200