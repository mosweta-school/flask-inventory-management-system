class InventoryItem:
    def __init__(
        self,
        id,
        barcode,
        product_name,
        brand,
        category,
        ingredients,
        price,
        stock,
    ):
        self.id = id
        self.barcode = barcode
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.ingredients = ingredients
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "barcode": self.barcode,
            "product_name": self.product_name,
            "brand": self.brand,
            "category": self.category,
            "ingredients": self.ingredients,
            "price": self.price,
            "stock": self.stock,
        }