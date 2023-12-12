# for loops

my_data = ["cars", "money", "women", "power"]

for item in my_data:
    print(item)

# iterating over dictionaries

my_dict = {
    "elements" : ["Ti", "Cu", "Au", "Fe"],
    "items": ["hood", "chasis", "wires", "jewelry"],
    "companies" : {
        "apple" : [
            "iphone", "ipad", "mac"
        ],
        "tesla": [
            "roadster", "model s", "model x", "cybertruck"
        ]
    }
}

for key, value in my_dict.items():
    print(f"Key: {key}")
    if isinstance(value, list):
        for element in value:
            print(f"  - {element}")
    elif isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(f"  Sub-Key: {sub_key}")
            
            if isinstance(sub_value, list):
                for element in sub_value:
                    print(f"    - {element}")
            else:
                print(f"    Sub-Value: {sub_value}")

    print() 

# there are various ways to unpack a dictionary
for item in my_dict.values():
    print(item)