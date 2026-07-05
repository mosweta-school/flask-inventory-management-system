def validate_inventory_data(data):
    """
    Validate inventory input.
    """

    barcode = data.get("barcode")
    price = data.get("price")
    stock = data.get("stock")

    if not barcode:
        return "Barcode is required"

    if price is None:
        return "Price is required"

    if price < 0:
        return "Price must be greater than or equal to zero"

    if stock is None:
        return "Stock is required"

    if stock < 0:
        return "Stock must be greater than or equal to zero"

    return None