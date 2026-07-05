from external.openfoodfacts import fetch_product_by_barcode, map_product

product = fetch_product_by_barcode("3017620422003")

print(map_product(product))