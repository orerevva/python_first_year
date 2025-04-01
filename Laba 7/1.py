import json
import jsonschema
from jsonschema import validate, ValidationError

with open("new_ex_1.json", 'r') as f:
    data = json.load(f)

with open("schema.json", "r") as f:
    schema = json.load(f)
try:
    validate(instance=data, schema=schema)
    print("JSON OK")
except ValidationError as e:
    print("ERROR:", e.message)

