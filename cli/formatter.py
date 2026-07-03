'''ui library'''
from rich.console import Console
from cli.theme import SUCCESS
from cli.theme import ERROR
from cli.theme import WARNING
from cli.theme import PRIMARY
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box





console = Console()


def print_header():

    console.print(
        Panel.fit(
            "[bold bright_cyan]Inventory Management System[/bold bright_cyan]\n"
            "[white]Administrator Portal[/white]",
            border_style=PRIMARY
        )
    )

    


def print_success(message):
    console.print(f"[{SUCCESS}]✓ {message}[/{SUCCESS}]")
    


def print_error(message):
    console.print(f"[{ERROR}]✗ {message}[/{ERROR}]")

    


def print_warning(message):
    console.print(f"[{WARNING}]⚠ {message}[/{WARNING}]")

def display_inventory(items):
    table = Table(
        title="📦 Inventory",
        box=box.ROUNDED,
        header_style="bold bright_cyan",
        show_lines=True
    )

    table.add_column("ID", justify="center", style="cyan", width=5)
    table.add_column("Product", style="white", width=25)
    table.add_column("Brand", style="green", width=18)
    table.add_column("Price", justify="right", style="yellow", width=10)
    table.add_column("Stock", justify="center", width=10)

    for item in items:

        stock = item["stock"]

        if stock >= 50:
            stock_text = Text(f"🟢 {stock}", style="green")

        elif stock >= 10:
            stock_text = Text(f"🟡 {stock}", style="yellow")

        else:
            stock_text = Text(f"🔴 {stock}", style="red")

        table.add_row(
            str(item["id"]),
            item["product_name"],
            item["brand"],
            f"${item['price']:.2f}",
            stock_text
        )

    console.print(table)

def display_product(item):

    body = f"""
[bold cyan]ID:[/bold cyan]           {item.get("id", "-")}
[bold cyan]Barcode:[/bold cyan]      {item.get("barcode", "-")}

[bold cyan]Product:[/bold cyan]      {item.get("product_name", "-")}
[bold cyan]Brand:[/bold cyan]        {item.get("brand", "-")}
[bold cyan]Category:[/bold cyan]     {item.get("category", "-")}

[bold cyan]Price:[/bold cyan]        ${item.get("price", 0):.2f}
[bold cyan]Stock:[/bold cyan]        {item.get("stock", "-")}

[bold cyan]Created:[/bold cyan]      {item.get("created_at", "-")}
[bold cyan]Updated:[/bold cyan]      {item.get("updated_at", "-")}
"""

    console.print(
        Panel(
            body,
            title="📄 Product Details",
            border_style="bright_blue",
            expand=False,
        )
    )