from rich.prompt import Prompt, IntPrompt, FloatPrompt

from cli.api import (
    get_inventory,
    get_item,
    add_item,
    update_item,
    delete_item,
    search_product,
)

from cli.formatter import (
    display_inventory,
    display_product,
    print_success,
    print_error,
    print_warning,
    console,
)
def view_inventory():
    items = get_inventory()

    if isinstance(items, dict) and "error" in items:
        print_error(items["error"])
        return

    if not items:
        print_warning("Inventory is empty.")
        return

    display_inventory(items)

def view_product():

    item_id = IntPrompt.ask("Enter Product ID")

    item = get_item(item_id)

    if "error" in item:
        print_error(item["error"])
        return

    display_product(item)

def search_openfoodfacts():

    barcode = Prompt.ask("Enter Barcode")

    with console.status(
        "[bold green]Searching OpenFoodFacts..."
    ):

        product = search_product(barcode)

    if "error" in product:
        print_error(product["error"])
        return

    display_product(product)

def add_product():

    barcode = Prompt.ask("Barcode")

    price = FloatPrompt.ask("Price")

    stock = IntPrompt.ask("Stock")

    with console.status(
        "[bold green]Adding product..."
    ):

        response = add_item(
            barcode,
            price,
            stock
        )

    if "error" in response:
        print_error(response["error"])
        return

    print_success("Product added successfully!")

    display_product(response)

def update_product():

    item_id = IntPrompt.ask("Product ID")

    price = FloatPrompt.ask("New Price")

    stock = IntPrompt.ask("New Stock")

    response = update_item(
        item_id,
        price,
        stock
    )

    if "error" in response:
        print_error(response["error"])
        return

    print_success("Product updated successfully!")

    display_product(response)

def delete_product():

    item_id = IntPrompt.ask("Product ID")

    confirm = Prompt.ask(
        "Are you sure you want to delete this product? (y/n)",
        choices=["y", "n"],
        default="n",
    )

    if confirm == "n":
        print_warning("Deletion cancelled.")
        return

    response = delete_item(item_id)

    if "error" in response:
        print_error(response["error"])
        return

    print_success(response["message"])