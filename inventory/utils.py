from datetime import datetime, timezone


def current_timestamp():
    return datetime.now(timezone.utc).isoformat()

def generate_inventory_id(inventory):
    """
    Generate the next available inventory ID.
    """

    if not inventory:
        return 1

    return max(item["id"] for item in inventory) + 1

