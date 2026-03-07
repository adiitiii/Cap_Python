def info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

data = {"name": "geeks for geeks", "age": 30, "country": "India"}
info(**data)