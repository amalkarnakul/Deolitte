from datetime import datetime



model_a = {
    "fname": "Alice",
    "dob": "1993-04-05",
    "location": "Pune"
}

model_b = {
    "first_name": "Alice",
    "birthDate": "05/04/1993",
    "city": "Pune"
}

mapping_config = {
    "model_a": {
        "fname": {"target": "name", "convert": None},
        "dob": {"target": "birth_date", "convert": "to_date_iso"},
        "location": {"target": "location", "convert": None}
    },
    "model_b": {
        "first_name": {"target": "name", "convert": None},
        "birthDate": {"target": "birth_date", "convert": "to_date_iso_from_ddmmyyyy"},
        "city": {"target": "location", "convert": None}
    }
}

def to_date_iso(date_str):
    # Expects YYYY-MM-DD
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except:
        return None

def to_date_iso_from_ddmmyyyy(date_str):
    # Expects DD/MM/YYYY
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except:
        return None

conversion_functions = {
    "to_date_iso": to_date_iso,
    "to_date_iso_from_ddmmyyyy": to_date_iso_from_ddmmyyyy
}

def unify_data(data, source_model):
    config = mapping_config[source_model]
    unified = {}
    for source_field, rule in config.items():
        value = data.get(source_field)
        if value is not None:
            if rule["convert"]:
                convert_func = conversion_functions.get(rule["convert"])
                if convert_func:
                    value = convert_func(value)
            unified[rule["target"]] = value
    return unified


unified_a = unify_data(model_a, "model_a")
unified_b = unify_data(model_b, "model_b")

print("Unified Model A:", unified_a)
print("Unified Model B:", unified_b)
