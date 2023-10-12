import csv
from pymongo import MongoClient
from row_fixer import fix_row

mongo_uri = TODO()
db_name = "helpy"
collection_name = "users"

client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

all_data = collection.find({})

csv_file = "output.csv"

field_names = list(all_data[0].keys())
# print(f"Field names: {field_names}")

with open(csv_file, mode='w', encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for row in all_data:
        row = fix_row(row)
        writer.writerow(row)

client.close()
