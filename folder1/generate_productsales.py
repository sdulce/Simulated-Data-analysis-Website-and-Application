import csv
import random

products = ['iPhone 16', 'MacBook Pro', 'iPad', 'Apple Watch']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

num_sales = 5000  # Number of sales records

with open('product_sales.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Product', 'Month', 'Units Sold'])
    writer.writeheader()

    for _ in range(num_sales):
        product = random.choice(products)
        month = random.choice(months)
        units_sold = random.randint(1, 5)  # 1 to 5 units per sale
        writer.writerow({
            'Product': product,
            'Month': month,
            'Units Sold': units_sold
        })
