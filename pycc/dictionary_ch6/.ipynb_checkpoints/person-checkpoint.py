person = {
    'name': 'Jamil',
    'age': 40,
    'occupation': 'Comedian',
    'main_work': 'Fatra Comedy',
    }

print(person['name'])
print(person['age'])
print(person['occupation'])
print(person["main_work"])

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1_000_000,
    'maggie': 0,
    }

num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")