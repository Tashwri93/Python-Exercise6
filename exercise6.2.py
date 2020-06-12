known_rivers = {
    'nile': 'egypt',
    'thames':'england',
    'jordan': 'israel'}

for river, country in known_rivers.items():
    print("The " + river.title()+ " runs through " + country.title())
