person_one = {
            'name': 'dylan',
             'lastname': 'kawende',
             'age': '23',
             'city': 'london'}

person_two = {
            'name': 'tashan',
             'lastname': 'wright-mckenzie',
             'age': '26',
             'city': 'london'}

person_three = {
            'name': 'van',
             'lastname': 'iswa',
             'age': '30',
             'city': 'watford'}


for title, details in person_one.items():
    print(title.title() + ": " + details.title())
