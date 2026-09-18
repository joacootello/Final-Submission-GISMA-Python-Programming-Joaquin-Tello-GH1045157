"""CUSTOMER MODULEE

This module has the Customer class and this represents one registered customer of the store
"""


class Customer:
    """registered customer of the store"""

    def __init__(self, customer_id, name, email, purchases, total_spent):
        """this creates a new customer.

        Arguments:
            customer_id: whole number that identifies the customer (int)
            name: full name of the customer (str)
            email: email address of the customer (str)
            purchases: how many sales this customer has made (int)
            total_spent: how much money this customer has spent (float)
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.purchases = purchases
        self.total_spent = total_spent

    def is_new_customer(self):
        """Return true in case this customer has not bought anything yet"""
        return self.purchases == 0

    def get_average_purchase(self):
        """Return the average amount of money spent per purchase

        Returns 0.0 when the customer has not bought anything, so that
        the program never divides by zero
        """
        if self.is_new_customer():
            return 0.0

        return self.total_spent / self.purchases

    def add_purchase(self, amount):
        """Record one more purchase and add its value to the total spent"""
        self.purchases = self.purchases + 1
        self.total_spent = self.total_spent + amount

    def show_info(self):
        """This prints the details of this customer on the screen"""
        print(f"ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

        if self.is_new_customer():
            print("Purchases: none yet")
        else:
            print(f"Purchases: {self.purchases}")
            print(f"Total spent: {self.total_spent:.2f}")
            print(f"Average purchase: {self.get_average_purchase():.2f}")

    def to_csv_row(self):
        """Return the data of this customer as a list, ready for a CSV."""
        return [self.customer_id, self.name, self.email,
                self.purchases, self.total_spent]