from flask import Blueprint, jsonify, request
from inventory.services import (
    add_item,
    delete_item,
    get_all_items,
    get_item,
    update_item,
)




inventory_bp = Blueprint("inventory", __name__)

"""
Inventory API routes.
"""
@inventory_bp.route("/inventory", methods=["GET"])
def fetch_inventory():
    return jsonify(get_all_items()), 200

@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def fetch_item(item_id):

    item = get_item(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200

@inventory_bp.route("/inventory", methods=["POST"])
def create_item():
    data = request.get_json()

    response, status = add_item(data)

    return jsonify(response), status


@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def patch_item(item_id):

    data = request.get_json()

    updated = update_item(item_id, data)

    if updated is None:
        return jsonify({"error":"Item not found"}),404

    return jsonify(updated),200

@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):

    deleted = delete_item(item_id)

    if not deleted:
        return jsonify({"error":"Item not found"}),404

    return jsonify({
        "message":"Item deleted successfully"
    }),200

