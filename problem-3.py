import csv

total_sales = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["qty"])
        price = int(row["price"])

        amount = quantity * price

        if product in total_sales:
            total_sales[product] += amount
        else:
            total_sales[product] = amount

print("Total Sales Amount for Each Product:")

for product, total in total_sales.items():
    print(product, ":", total)
