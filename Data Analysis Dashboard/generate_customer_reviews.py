import csv
import random

products = ['iPhone 16', 'MacBook Pro', 'iPad', 'Apple Watch']
num_reviews = 5000

# Weighted star distribution: more 5s and 4s
rating_weights = [1, 2, 3, 4, 5]
probabilities = [0.05, 0.10, 0.15, 0.30, 0.40]  # Skewed toward higher stars

with open('customer_reviews.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Product', 'Rating'])
    writer.writeheader()

    for _ in range(num_reviews):
        product = random.choice(products)
        rating = random.choices(rating_weights, probabilities)[0]
        writer.writerow({'Product': product, 'Rating': rating})
