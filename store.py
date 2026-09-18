"""Store module.

This module contains the Store class. The Store keeps the lists of vinyls,
customers and sales, and it is also responsible for reading and writing the
CSV files where the data is kept between runs of the program.
"""

import csv

from customer import Customer
from sale import Sale
from vinyl import Vinyl

# Names of the three data files. They are written in capital letters
# because they are constants: their value never changes while the
# program is running.
VINYLS_FILE = "vinyls.csv"
CUSTOMERS_FILE = "customers.csv"
SALES_FILE = "sales.csv"


class Store:
    """The vinyl record shop, with its catalogue, customers and sales."""

    def __init__(self, name):
        """Create an empty store.

        Arguments:
            name -- the name of the shop (str)
        """
        self.name = name
        self.vinyls = []
        self.customers = []
        self.sales = []

    # ------------------------------------------------------------------
    # Searching
    # ------------------------------------------------------------------

    def find_vinyl(self, vinyl_id):
        """Return the vinyl with this ID, or None if it does not exist."""
        for vinyl in self.vinyls:
            if vinyl.vinyl_id == vinyl_id:
                return vinyl

        return None

    def find_customer(self, customer_id):
        """Return the customer with this ID, or None if it does not exist."""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    # ------------------------------------------------------------------
    # Showing information
    # ------------------------------------------------------------------

    def show_vinyls(self):
        """Print every vinyl record in the catalogue."""
        if len(self.vinyls) == 0:
            print("There are no vinyl records in the catalogue yet.")
            return

        print()
        print("--- VINYL CATALOGUE ---")
        for vinyl in self.vinyls:
            print()
            vinyl.show_info()

    def show_customers(self):
        """Print every registered customer."""
        if len(self.customers) == 0:
            print("There are no registered customers yet.")
            return

        print()
        print("--- REGISTERED CUSTOMERS ---")
        for customer in self.customers:
            print()
            customer.show_info()

    # ------------------------------------------------------------------
    # Adding data
    # ------------------------------------------------------------------

    def add_vinyl(self, title, artist, price, stock):
        """Add a vinyl to the catalogue and return it.

        If the same album by the same artist is already in the catalogue,
        the new copies are added to the existing record instead of creating
        a second entry with a different ID.
        """
        for vinyl in self.vinyls:
            if vinyl.title.lower() == title.lower():
                if vinyl.artist.lower() == artist.lower():
                    vinyl.restock(stock)
                    self.save_vinyls()
                    return vinyl

        # Work out the next free ID: one more than the highest ID in use.
        new_id = 1
        for vinyl in self.vinyls:
            if vinyl.vinyl_id >= new_id:
                new_id = vinyl.vinyl_id + 1

        new_vinyl = Vinyl(new_id, title, artist, price, stock)
        self.vinyls.append(new_vinyl)
        self.save_vinyls()
        return new_vinyl

    def register_customer(self, name, email):
        """Create a new customer, save it and return it."""
        new_id = 1
        for customer in self.customers:
            if customer.customer_id >= new_id:
                new_id = customer.customer_id + 1

        new_customer = Customer(new_id, name, email, 0, 0.0)
        self.customers.append(new_customer)
        self.save_customers()
        return new_customer

    def make_sale(self, customer, vinyl, quantity):
        """Register a sale of one vinyl to one customer.

        Returns the Sale object if the sale was completed, or None if the
        quantity was not valid or there was not enough stock.
        """
        new_id = 1
        for sale in self.sales:
            if sale.sale_id >= new_id:
                new_id = sale.sale_id + 1

        new_sale = Sale(new_id, customer.customer_id, vinyl.vinyl_id,
                        quantity, vinyl.price)

        if not new_sale.is_valid_quantity():
            return None

        if not vinyl.reduce_stock(quantity):
            return None

        new_sale.calculate_total()
        customer.add_purchase(new_sale.total)
        self.sales.append(new_sale)

        # The sale changed the stock, the customer and the sales list,
        # so all three files have to be written again.
        self.save_all()
        return new_sale

    # ------------------------------------------------------------------
    # Reading the CSV files
    # ------------------------------------------------------------------

    def load_vinyls(self):
        """Read the vinyl catalogue from its CSV file."""
        try:
            with open(VINYLS_FILE, "r", newline="",
                      encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if len(row) == 5:
                        vinyl = Vinyl(int(row[0]), row[1], row[2],
                                      float(row[3]), int(row[4]))
                        self.vinyls.append(vinyl)
        except FileNotFoundError:
            print(f"File {VINYLS_FILE} not found. Starting with no vinyls.")

    def load_customers(self):
        """Read the customer list from its CSV file."""
        try:
            with open(CUSTOMERS_FILE, "r", newline="",
                      encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if len(row) == 5:
                        customer = Customer(int(row[0]), row[1], row[2],
                                            int(row[3]), float(row[4]))
                        self.customers.append(customer)
        except FileNotFoundError:
            print(f"File {CUSTOMERS_FILE} not found. Starting with no "
                  f"customers.")

    def load_sales(self):
        """Read the sales history from its CSV file."""
        try:
            with open(SALES_FILE, "r", newline="",
                      encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if len(row) == 6:
                        sale = Sale(int(row[0]), int(row[1]), int(row[2]),
                                    int(row[3]), float(row[4]))
                        sale.total = float(row[5])
                        self.sales.append(sale)
        except FileNotFoundError:
            print(f"File {SALES_FILE} not found. Starting with no sales.")

    def load_all(self):
        """Read the three data files when the program starts."""
        self.load_vinyls()
        self.load_customers()
        self.load_sales()

    # ------------------------------------------------------------------
    # Writing the CSV files
    # ------------------------------------------------------------------

    def save_vinyls(self):
        """Write the whole vinyl catalogue to its CSV file."""
        with open(VINYLS_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for vinyl in self.vinyls:
                writer.writerow(vinyl.to_csv_row())

    def save_customers(self):
        """Write the whole customer list to its CSV file."""
        with open(CUSTOMERS_FILE, "w", newline="",
                  encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for customer in self.customers:
                writer.writerow(customer.to_csv_row())

    def save_sales(self):
        """Write the whole sales history to its CSV file."""
        with open(SALES_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for sale in self.sales:
                writer.writerow(sale.to_csv_row())

    def save_all(self):
        """Write the three data files."""
        self.save_vinyls()
        self.save_customers()
        self.save_sales()
