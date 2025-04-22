import csv
import random

regions = {
    'North America': ['New York', 'San Francisco', 'Los Angeles', 'Toronto', 'Chicago'],
    'Europe': ['London', 'Paris', 'Berlin', 'Milan', 'Madrid'],
    'Asia-Pacific': ['Tokyo', 'Seoul', 'Shanghai', 'Beijing', 'Sydney'],
    'Latin America': ['São Paulo', 'Buenos Aires', 'Mexico City', 'Lima'],
    'Middle East & Africa': ['Dubai', 'Istanbul', 'Cairo', 'Johannesburg']
}

store_id = 1
total_stores = 100  # You can increase this for larger datasets

with open('revenue_by_region.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Store Name', 'Region', 'Revenue ($M)'])
    writer.writeheader()

    for _ in range(total_stores):
        region = random.choice(list(regions.keys()))
        city = random.choice(regions[region])
        store_name = f"Apple {city} #{store_id:03}"

        # Simulate revenue based on region
        base = {
            'North America': random.uniform(80, 150),
            'Europe': random.uniform(70, 130),
            'Asia-Pacific': random.uniform(75, 140),
            'Latin America': random.uniform(30, 80),
            'Middle East & Africa': random.uniform(40, 90)
        }

        revenue = round(base[region], 2)

        writer.writerow({
            'Store Name': store_name,
            'Region': region,
            'Revenue ($M)': revenue
        })

        store_id += 1
