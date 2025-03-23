import json

with open("Sample-JSON-file-with-multiple-records.json", "r", encoding="utf-8") as f:
    data = json.load(f)

root_key = list(data.keys())[0]
records = data[root_key]

if records:
    headers = list(records[0].keys())

    csv_file = root_key + ".csv"

    with open(csv_file, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n") 
        for record in records:
            f.write(",".join(str(record[h]) for h in headers) + "\n")  

    print(f"OK: {csv_file}")
else:
    print("ERROR")