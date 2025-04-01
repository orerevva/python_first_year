import json
f_path = 'ex_2.json'
with open(f_path, 'r', encoding='utf-8') as file:
    raw_data = file.read()

form_json = json.dumps(json.loads(f'[{raw_data}]'), indent=4, ensure_ascii=False)
form_f_path = 'form_ex_2.json'
with open(form_f_path, 'w', encoding='utf-8') as form_f:
    form_f.write(form_json)

data = json.loads(f'[{raw_data}]')
users_dict = {user["name"]: user["phoneNumber"] for user in data}

print(users_dict)

output_f_path = 'users_phones.json'
with open(output_f_path, 'w', encoding='utf-8') as output_file:
    json.dump(users_dict, output_file, indent=4, ensure_ascii=False)
