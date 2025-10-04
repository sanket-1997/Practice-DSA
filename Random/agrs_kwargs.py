def details(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

person = {"name": "David", "agje": 40, "city": "New York"}

#details(**person)   # dictionary unpacked into keyword arguments
print(*person)