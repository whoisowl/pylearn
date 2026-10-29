import csv

input_file = "products.csv"
output_file = "processed_products.csv"

products = []
grand_total = 0

with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Product Name"]
        price = float(row["Price"])
        quantity = int(row["Quantity"])

        total_price = price * quantity
        grand_total += total_price

        products.append(
            {
                "Product Name": name,
                "Price": price,
                "Quantity": quantity,
                "Total Price": total_price,
            }
        )

with open(output_file, "w", newline="", encoding="utf-8-sig") as file:
    fieldnames = ["Product Name", "Price", "Quantity", "Total Price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

print(f"Processed {len(products)} products successfully!")
print(f"Grand total inventory value: {grand_total:,.2f}")
print(f"Output saved to {output_file}")
