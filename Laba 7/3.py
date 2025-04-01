import json

f_path = 'ex_3.json'
with open(f_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {"name": "item 4", "quantity": 3, "price": 30.00},
        {"name": "item 5", "quantity": 1, "price": 60.00}
    ]
}

data["invoices"].append(new_invoice)

new_f = 'new_ex_3.json'
with open(new_f, 'w', encoding='utf-8') as updated_file:
    json.dump(data, updated_file, indent=4, ensure_ascii=False)

