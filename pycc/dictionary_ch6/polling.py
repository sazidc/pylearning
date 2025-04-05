favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'java',
    'edward': 'python'
}

polling_language = ['jenny', 'sarah', 'erin', 'phil']

for people in polling_language:
    if people.lower() in favorite_languages.keys():
        print(f"Thanks {people.title()}, for taking the poll")
    elif people.lower() not in favorite_languages.keys():
        print(f"{people.title()}, you are invited to take the poll")
