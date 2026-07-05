from rich.console import Console
from rich.prompt import Prompt

from cli.menu import display_menu
from cli.commands import (
    view_inventory,
    view_product,
    add_product,
    update_product,
    delete_product,
    search_openfoodfacts,
)

console = Console()


def main():
    """Entry point for the Inventory Management CLI."""

    while True:
        console.clear()

        display_menu()

        choice = Prompt.ask(
            "\n[bold cyan]Select an option[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6", "7"],
            default="7",
        )

        try:
            match choice:

                case "1":
                    view_inventory()

                case "2":
                    view_product()

                case "3":
                    add_product()

                case "4":
                    update_product()

                case "5":
                    delete_product()

                case "6":
                    search_openfoodfacts()

                case "7":
                    console.print(
                        "\n[bold green]Thank you for using the Inventory Management System![/bold green]"
                    )
                    break

        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")

        except Exception as e:
            console.print(f"\n[bold red]Unexpected error:[/bold red] {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()