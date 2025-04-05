favorite_places = {
    'sarah': ['nile', 'amazon', 'kirtonkhola'],
    'jenny': ['nile', 'amazon', 'kirtonkhola'],
    'erin': ['nile', 'amazon', 'kirtonkhola'],
    'phil': ['nile', 'amazon', 'kirtonkhola'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")