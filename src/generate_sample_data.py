import csv
import os

####### GENERATE CUSTOMERS CSV FILE ########
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(project_dir, "data", "raw")
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, "customers.csv")


header = [
    'customer_id', 'first_name', 'last_name', 'email', 'city', 'registration_date'
]

customers = [
    [1001, 'Maria', 'Santos', 'maria.santos@example.com','Manila','2026-01-15'],
    [1002, 'Juan', 'Reyes', 'juan.reyes@example.com', 'Quezon City', '2026-01-20'],
    [1003, 'Ana', 'Cruz', 'ana.cruz@example.com', 'Cebu City', '2026-02-02'],
    [1004, 'Mark', 'Garcia', 'mark.garcia@example.com', 'Davao City', '2026-02-10'],
    [1005, 'Sofia', 'Mendoza', 'sofia.mendoza@example.com', 'Manila', '2026-03-05']
]


with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header) # Put Header in the first row
    writer.writerows(customers) # Put the rest of the records in the following rows



# ####### GENERATE PRODUCTS CSV FILE ########
products_header = [
    'product_id', # Unique product identifier
    'product_name', # Product name
    'category', # Product category
    'unit_price', # Selling price per unit
    'stock_quantity' # Available stock   
]

products_values = [
    [2001, 'Wireless Mouse', 'Electronics', 850.00, 120],
    [2002, 'Bluetooth Headphones', 'Electronics', 1_500.00, 80],
    [2003, 'Smartphone Stand', 'Accessories', 350.00, 150],
    [2004, 'USB-C Hub', 'Electronics', 1_200.00, 60],
    [2005, 'Portable Charger', 'Electronics', 1_800.00, 90]
]
file_path = os.path.join(output_dir, "products.csv")
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(products_header) # Put Header in the first row
    writer.writerows(products_values) # Put the rest of the records in the following rows




# ####### GENERATE STORES CSV FILE ########
stores_header = [
    'store_id', # Unique integer, starting at 3001
    'store_name', # Store name, e.g. Manila Central
    'city', # Philippine city
    'region', # Philippine region
    'opening_date' # Date in YYYY-MM-DD format   
]

stores_values = [
    [3001, 'Manila Central', 'Manila', 'NCR', '2025-01-15'],
    [3002, 'Cebu City Mall', 'Cebu City', 'Central Visayas', '2025-02-20'],
    [3003, 'Davao Downtown', 'Davao City', 'Davao Region', '2025-03-10'],
    [3004, 'Quezon City Plaza', 'Quezon City', 'NCR', '2025-04-05'],
    [3005, 'Baguio City Center', 'Baguio City', 'Cordillera Administrative Region', '2025-05-15']   
]


file_path = os.path.join(output_dir, "stores.csv")
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(stores_header) # Put Header in the first row
    writer.writerows(stores_values) # Put the rest of the records in the following rows




# ####### GENERATE SALES CSV FILE ########
sales_header = [
    'sale_id', # unique integers from 4001 through 4010
    'sale_date', # dates between 2026-01-01 and 2026-03-31
    'customer_id', # use IDs 1001–1005 from your customer dataset
    'product_id', # use IDs 2001–2005 from your product dataset
    'store_id', # use IDs 3001–3005 from your store dataset  
    'quantity', # positive integers
    'unit_price', # match the selected product's price
    'total_amount' # calculate quantity × unit_price
]

sales_values = [
    [4001, '2026-01-05', 1001, 2001, 3001, 2, 850.00, 1700.00],
    [4002, '2026-01-10', 1002, 2002, 3002, 1, 1500.00, 1500.00],
    [4003, '2026-01-15', 1003, 2003, 3003, 3, 350.00, 1050.00],
    [4004, '2026-01-20', 1004, 2004, 3004, 1, 1200.00, 1200.00],
    [4005, '2026-01-25', 1005, 2005, 3005, 2, 1800.00, 3600.00],
    [4006, '2026-02-05', 1001, 2001, 3001, 1, 850.00, 850.00],
    [4007, '2026-02-10', 1002, 2002, 3002, 2, 1500.00, 3000.00],
    [4008, '2026-02-15', 1003, 2003, 3003, 1, 350.00, 350.00],
    [4009, '2026-02-20', 1004, 2004, 3004, 3, 1200.00, 3600.00],
    [4010,'2026-02-25',1005 ,2005 ,3005 ,1 ,1800.00 ,1800.00]
]


file_path = os.path.join(output_dir, "sales.csv")
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(sales_header) # Put Header in the first row
    writer.writerows(sales_values) # Put the rest of the records in the following rows
