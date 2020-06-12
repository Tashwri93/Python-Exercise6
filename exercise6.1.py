glossary = {
    'lists': 'data stored in a list',
    'tuple': 'like a list but cannot be manipulated',
    'dictionary': 'collection of key value pairs',
    'if statements': 'set of conditions',
    'variables': 'data which can be assigned to a value'}

print("Lists: " + glossary['lists']
      +"\nTuples: " + glossary['tuple']
      +"\nDictionary: " + glossary['dictionary']
      +"\nIf statements: " + glossary['if statements'])

print("\n")

glossary['loop'] = 'it does repetitve tasks efficiently'

for name, definition in glossary.items():
    print(name.title() + ": " + definition.title())
