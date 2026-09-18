"""VINYL MODULEE

This part of the program is responsible of having the Vinyl class, this represents vinil record sold by the company
"""


class Vinyl:
    """A single vinyl record in the store catalogue"""

    def __init__(self, vinyl_id, title, artist, price, stock):
        """This creates a new vinyl record

        Arguments:
            vinyl_id: whole number that identifies the record (int)
            title: name of the album (str)
            artist: name of the artist or band (str)
            price: price of one copy, in euros (float)
            stock: number of copies available in the shop (int)
        """
        self.vinyl_id = vinyl_id
        self.title = title
        self.artist = artist
        self.price = price
        self.stock = stock

    def show_info(self):
        """Print all the details of this vinyl record on the screen"""
        print(f"ID: {self.vinyl_id}")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Price: {self.price:.2f}")
        print(f"Stock: {self.stock}")

    def is_available(self, quantity):
        """Return True just in case the shop has enough copies for this quantity"""
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        """Then remove copies from the stock after a sale

        It returns true if the stock was reduced and false if there were
        not enough copies
        """
        if self.is_available(quantity):
            self.stock = self.stock - quantity
            return True

        return False

    def restock(self, quantity):
        """Add more copies of this record to the stock"""
        self.stock = self.stock + quantity

    def to_csv_row(self):
        """Return the data of this vinyl as a list, it is ready to save in a CSV"""
        return [self.vinyl_id, self.title, self.artist, self.price, self.stock]
