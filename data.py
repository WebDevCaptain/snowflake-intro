import csv

data = [
    [1, "Alice", "alice@example.com", 28, "New York"],
    [2, "Bob", "bob@example.com", 35, "San Francisco"],
    [3, "Charlie", "charlie@example.com", 40, "Los Angeles"],
    [4, "David", "david@example.com", 22, "Chicago"],
    [5, "Emma", "emma@example.com", 30, "Miami"],
    [6, "Frank", "frank@example.com", 26, "Boston"],
    [7, "Grace", "grace@example.com", 33, "Seattle"],
    [8, "Hank", "hank@example.com", 45, "Denver"],
    [9, "Ivy", "ivy@example.com", 29, "Austin"],
    [10, "Jack", "jack@example.com", 27, "Houston"],
]

with open("customers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "email", "age", "city"])  # Header
    writer.writerows(data)

print("CSV file 'customers.csv' created.")
