import csv
import random

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open('sales_trends.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Month', 'Trend Index'])
    writer.writeheader()
    trend = 100
    for month in months:
        trend += random.randint(-10, 20)
        writer.writerow({
            'Month': month,
            'Trend Index': trend
        })
