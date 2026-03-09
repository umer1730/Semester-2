import csv
import random
import config


def load_data(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            data.append(row)
    return data


def filter_data(data):
    filtered = []
    for row in data:
        quantity = int(row[2])
        if quantity > config.THRESHOLD:
            filtered.append(row)
    return filtered


def sample_data(data):
    random.seed(config.RANDOM_SEED)
    k = int(len(data) * config.SAMPLE_FRACTION)
    return random.sample(data, k)


def write_data(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "product", "quantity", "price"])
        writer.writerows(data)


def compute_revenue(data):
    revenue = {}
    for row in data:
        product = row[1]
        quantity = float(row[2])
        price = float(row[3])

        total = quantity * price

        if product not in revenue:
            revenue[product] = []
        revenue[product].append(total)

    return revenue


def print_summary(revenue):
    print("Average Revenue Per Product")
    for product, values in revenue.items():
        avg = sum(values) / len(values)
        print(product, ":", avg)

if __name__ == "__main__":
    data = load_data(config.INPUT_FILE)
    filtered = filter_data(data)
    sampled = sample_data(filtered)
    write_data(config.OUTPUT_FILE, sampled)
    revenue = compute_revenue(sampled)
    print_summary(revenue)