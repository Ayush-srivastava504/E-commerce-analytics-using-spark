from faker import Faker
import random
import csv

fake = Faker()

batch_size = 100_000     #  REDUCED
total_batches = 10       # 10 × 100k = 1M rows

for batch in range(total_batches):
    filename = f"orders_part_{batch}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "order_id", "customer_id", "product_id", "order_timestamp",
            "quantity", "unit_price", "discount", "payment_type",
            "order_status", "city"
        ])

        for i in range(batch_size):
            writer.writerow([
                f"O{batch}_{i}",
                f"C{random.randint(1, 500000)}",
                f"P{random.randint(1, 20000)}",
                fake.date_time_between(start_date="-3y"),
                random.randint(1, 5),
                round(random.uniform(100, 5000), 2),
                round(random.uniform(0, 0.4), 2),
                random.choice(["UPI", "CARD", "COD", "WALLET"]),
                random.choice(["PLACED", "PAID", "SHIPPED", "DELIVERED", "CANCELLED"]),
                fake.city()
            ])

    print(f" Generated {filename}")
