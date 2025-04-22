import csv
import random

with open('store_revenue_vs_pricing.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Store ID', 'Avg Product Price ($)', 'Revenue ($M)'])
    writer.writeheader()

    for i in range(1, 301):  # 300 stores
        avg_price = random.randint(900, 1500)  # Simulated average price of products in store
        revenue = avg_price * random.uniform(0.03, 0.06)  # Revenue scales loosely with price
        writer.writerow({
            'Store ID': f'ST-{i:03}',
            'Avg Product Price ($)': round(avg_price, 2),
            'Revenue ($M)': round(revenue, 2)
        })
