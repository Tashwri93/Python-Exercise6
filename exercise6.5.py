people = []

person = {
            'name': 'dylan',
             'lastname': 'kawende',
             'age': 23,
             'city': 'london'}

people.append(person)

person = {
            'name': 'tashan',
             'lastname': 'wright-mckenzie',
             'age': 26,
             'city': 'london'}
people.append(person)

person= {
            'name': 'van',
             'lastname': 'iswa',
             'age': 30,
             'city': 'watford'}

people.append(person)


for person in people:
    name = person['name'].title() + " " + person['lastname'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is "+ age +" years old.")
