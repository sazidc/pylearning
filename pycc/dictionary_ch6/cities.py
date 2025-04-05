cities = {
    'London' : ['United Kingndom', '8.9 Million', 'London is the capital of England'],
    'New York' : ['United States', '8.9 Million', 'New York is the capital of New York'],
    'Tokyo' : ['Japan', '8.9 Million', 'Tokyo is the capital of Japan'],
    'Shanghai' : ['China', '8.9 Million', 'Shanghai is the capital of China'],
    'Mumbai' : ['India', '8.9 Million', 'Mumbai is the capital of India']
}

# print(f"Facts about {list(cities.keys())[0]} is {cities['London']}")

for key, value in cities.items():
    print(f"Three Facts about {key} is {value}")