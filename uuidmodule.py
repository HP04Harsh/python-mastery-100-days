import uuid

items = [['laptop', 1200],
         ['mouse', 20],
         ['keyboard', 30],
         ['tablet', 200]]

item_data = {}

for i in items:
    id = uuid.uuid5(uuid.NAMESPACE_OID,i[0]) //uuid intialize
    key = id.hex[:3] //only we want 3 uuid
    item_data[key] = i  // assign key to dictonary


print("Item Data:")
for k, v in item_data.items():
    print(f"{k}: {v}")
