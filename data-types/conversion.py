# type conversion
def convert_data_type(input_data: any, output_type: str = "string"):
    annotations = {
        "string": str,
        "str": str,
        "int": int,
        "number": int,
        "float": float,
        "decimal": float,
    }
    
    if output_type not in annotations.keys():
        return None
    
    try:
        return annotations[output_type](input_data)
    except ValueError as e:
        print(str(e))
        return None
    

print(convert_data_type("11", "int"))