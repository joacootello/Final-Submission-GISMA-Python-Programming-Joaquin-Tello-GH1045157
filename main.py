"""This is the main module of the program

This is the one u have to execute to start the program because it has the menu and its the only one that talks to the
user


Run it with:  py main.py
"""

from store import Store


def read_text(message):
    """Ask the user for a piece of text and remove the extra spaces"""
    return input(message).strip()


def read_int(message):
    """Ask the user for a whole number

   IF the user types something that is not a whole number return it, try / except is used so that the program shows
   a message instead of crashing
    """
    text = input(message)
    try:
        return int(text)
    except ValueError:
        print("Error: that is not a valid whole number.")
        return None


def read_float(message):
    """Ask the user for a decimal number.

    Returns the number, or None if the user typed something that is not a
    number, for example the word "hello" instead of 29.99.
    """
    text = input(message)
    try:
        return float(text)
    except ValueError:
        print("Error: that is not a valid price.")
        return None


def show_menu():
    """Print the main menu on the screen."""
    print()
    print("==============================")
    print("      VINYL RECORD STORE")
    print("==============================")
    print("1. View vinyls")
    print("2. Add vinyl")
    print("3. View customers")
    print("4. Register customer")
    print("5. Make sale")
    print("6. Exit")
    print()


def do_add_vinyl(store):
    """Ask the user for the details of a vinyl and add it to the store"""
    title = read_text("Album title: ")
    if title == "":
        print("Error: the title cannot be empty")
        return

    artist = read_text("Artist: ")
    if artist == "":
        print("Error: the artist cannot be empty")
        return

    price = read_float("Price: ")
    if price is None:
        return

    if price <= 0:
        print("Error: the price must be greater than zero")
        return

    stock = read_int("Stock: ")
    if stock is None:
        return

    if stock <= 0:
        print("Error: the stock must be greater than zero")
        return

    vinyl = store.add_vinyl(title, artist, price, stock)
    print()
    print("Vinyl saved successfully.")
    print(f"'{vinyl.title}' now has {vinyl.stock} copies in stock")


def do_register_customer(store):
    """Ask the user for the details of a customer and register them."""
    name = read_text("Customer name: ")
    if name == "":
        print("Error: the name cannot be empty.")
        return

    email = read_text("Email: ")
    if email == "":
        print("Error: the email cannot be empty.")
        return

    customer = store.register_customer(name, email)
    print()
    print("Customer registered successfully.")
    print(f"Customer ID: {customer.customer_id}")


def do_make_sale(store):
    """Ask the user for the details of a sale and register it"""
    customer_id = read_int("Customer ID: ")
    if customer_id is None:
        return

    customer = store.find_customer(customer_id)
    if customer is None:
        print("Error: there is no customer with that ID")
        return

    vinyl_id = read_int("Vinyl ID: ")
    if vinyl_id is None:
        return

    vinyl = store.find_vinyl(vinyl_id)
    if vinyl is None:
        print("Error: there is no vinyl with that ID")
        return

    quantity = read_int("Quantity: ")
    if quantity is None:
        return

    if not vinyl.is_available(quantity):
        print(f"Error: not enough stock. Only {vinyl.stock} copies left")
        return

    sale = store.make_sale(customer, vinyl, quantity)
    if sale is None:
        print("Error: the quantity must be greater than zero")
        return

    print()
    sale.show_info(vinyl.title)
    print("Sale completed successfully.")
    print(f"New stock of '{vinyl.title}': {vinyl.stock}")


def main():
    """Start the program and repeat the menu until the user exits"""
    store = Store("Vinyl Record Store")
    store.load_all()

    running = True
    while running:
        show_menu()
        option = read_text("Select an option: ")

        if option == "1":
            store.show_vinyls()
        elif option == "2":
            do_add_vinyl(store)
        elif option == "3":
            store.show_customers()
        elif option == "4":
            do_register_customer(store)
        elif option == "5":
            do_make_sale(store)
        elif option == "6":
            print("Chao chao it was a pleasure enjoy your NEW vinyls :))) !")
            running = False
        else:
            print("Invalid option. Please just choose a number from 1 to 6.")


# This line makes sure that main() only runs when this file is executed
# directly, and not when it is imported from another file.
if __name__ == "__main__":
    main()
