from rich.console import Console
from rich.table import Table
from cli.formatter import print_header

console = Console()


def display_menu():

    print_header()

    table = Table(
        title="Main Menu",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Option", justify="center", width=10)
    table.add_column("Action")

    table.add_row("1", "📦 View Inventory")
    table.add_row("2", "🔍 View Product")
    table.add_row("3", "➕ Add Product")
    table.add_row("4", "✏ Update Product")
    table.add_row("5", "❌ Delete Product")
    table.add_row("6", "🌍 Search OpenFoodFacts")
    table.add_row("7", "🚪 Exit")

    console.print(table)

