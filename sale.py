"""SALE MODULEE

This module has the sale class, this represents one sale of the store to a customer.

After a sale the ID of the customer that bought it is saved with the ID of the vinyl, this is because the data is
saved in a flat CSV file than only holds simple values

"""


class Sale:
    """One sale of a vinyl record to a customer"""

    def __init__(self, sale_id, customer_id, vinyl_id, quantity, unit_price):
        """Create a new sale.

        Arguments:
            sale_id: whole number that identifies the sale (int)
            customer_id: ID of the customer who bought (int)
            vinyl_id: ID of the vinyl that was sold (int)
            quantity: number of copies sold (int)
            unit_price: price of one copy at the time of the sale (float)

        The total starts at 0.0 since there are no purchases yet and is worked out by calculate_total().
        """
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.vinyl_id = vinyl_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total = 0.0

    def is_valid_quantity(self):
        """WIll return true if the customer is buying at least one copy."""
        return self.quantity > 0

    def calculate_total(self):
        """Work out the total price of the sale then store it and return it"""
        self.total = self.unit_price * self.quantity
        return self.total

    def show_info(self, vinyl_title):
        """Print a simple receipt for this sale

        The title of the album is received as an argument because the sale
        only stores its ID, not the vinyl
        """
        print("--- RECEIPT ---")
        print(f"Sale ID: {self.sale_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Vinyl: {vinyl_title}")
        print(f"Quantity: {self.quantity}")
        print(f"Unit price: {self.unit_price:.2f}")
        print(f"Total: {self.total:.2f}")
        print("---------------")

    def to_csv_row(self):
        """Return the data of this sale as a list, it is ready for a CSV"""
        return [self.sale_id, self.customer_id, self.vinyl_id,
                self.quantity, self.unit_price, self.total]
