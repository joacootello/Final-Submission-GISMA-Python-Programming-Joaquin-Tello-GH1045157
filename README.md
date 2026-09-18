# Vinyl Store Management System

## Purpose

This is a command list application for an independent small Vinyl store

Normally when you go to vinyl stores you have to go through all the vinyls without even knowing if the store has the
one you are looking for, normally these small stores take notes manually in paper which makes its slower for them to work, this also makes the work unefficient. This system looks to solve this small but tedious issues small business
usually face. The first one being nobody knowing what the real stock is which could cause them to sell a product they currently dont have. And the second one being loosing sales history.

With every sale done the program automatically registers it updating the stock of the product. This information is saved un CSV files, this way it keeps being there the next time the program is being used.

The scope is small. Manage a catalogue including its customers and sales. It does not process payments and does not manage emplyees or supppliers.


## Installation and execution

The program only uses modules from the Python standard library, so this way there is nothing to install

The only requirement is: Python 3.8 or newer.

Then you have to:
1. Download or clone this repository.
2. Open a terminal inside the project folder.
3. Run the program:
then type py main.py



IMPORTANT: The program must be run from inside the project folder, because it reads and
writes the three CSV files using relative file names.

## Example usage

```
==============================
      VINYL RECORD STORE
==============================
1. View vinyls
2. Add vinyl
3. View customers
4. Register customer
5. Make sale
6. Exit

Select an option: 5
Customer ID: 3
Vinyl ID: 5
Quantity: 2

--- RECEIPT ---
Sale ID: 1
Customer ID: 3
Vinyl: La vida lenta
Quantity: 2
Unit price: 39.99
Total: 79.98
---------------
Sale completed successfully.
New stock of 'La vida lenta': 2
```

If the customer asks for more copies than the shop has, the sale is refused and
the stock is left untouched:

```
Select an option: 5
Customer ID: 2
Vinyl ID: 3
Quantity: 99
Error: not enough stock. Only 5 copies left.
```

## Key features

- **View vinyls** — this shows all the vinyls available including artist, album name, price and stock
- **Add vinyl** — adds a new album to the catalogue. But ff the same album by the
  same artist already exists then the new copies are added to the existing record
  instead of creating a duplicate one
- **View customers** — lists every registered customer, with the number of
  purchases and the total amount spent
- **Register customer** — this registers a new customer and assigns an ID
  automatically (for example ID:6)
- **Make sale** — registers a sale, then checks that everything is valid including customer, the album and the
  quantity, checks that there is enough stock, calculates the total,
  reduces the stock and updates the customer's purchase history.
- **Persistent data** — all the information is stored in CSV files and reloaded
  automatically when the program starts
- **Error handling** — invalid prices, invalid quantities, unknown IDs, empty
  fields, insufficient stock and missing data files are all handled with a
  message instead of a crash


## Project files

'main.py' - Entry point. Contains the menu and all the user interaction
'vinyl.py' - The `Vinyl` class: one album in the catalogue
'customer.py' - The `Customer` class: one registered customer
'sale.py' - The `Sale` class: one completed sale
'store.py' - The `Store` class: this holds the data and reads/writes the CSV files
'vinyls.csv' - Sample catalogue data
'customers.csv' - Sample customer data
'sales.csv' - Sales history


## References

- Python Software Foundation (2024) *csv — CSV File Reading and Writing*.
  Available at: https://docs.python.org/3/library/csv.html
- Python Software Foundation (2024) *Errors and Exceptions*. Available at:
  https://docs.python.org/3/tutorial/errors.html
- van Rossum, G., Warsaw, B. and Coghlan, N. (2001) *PEP 8 — Style Guide for
  Python Code*. Available at: https://peps.python.org/pep-0008/
