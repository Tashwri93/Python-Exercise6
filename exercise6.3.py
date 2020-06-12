favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'}

poll = ['erin', 'sarah', 'tash', 'jen', 'edward', 'phil']

for name in poll:
    if name not in favourite_languages.keys():
        print(name.title() + ", please take part of our poll!")
    else:
        print(name.title() + ", thank you for taking part of our poll!") 
