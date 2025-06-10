name = 'psalm ntiforo'
print(name.title())
print(name.lower())
print(name.upper())

first_name = 'psalm'
other_name = 'helene'
last_name = 'ntiforo'
print(f'{first_name} {other_name} {last_name}')
print(f'Hi {last_name} {first_name} {other_name}')
print(f'Bonjour {last_name.upper()} {first_name.title()} {other_name.lower()}')
greeting = f'Buenas tardes, {first_name.title()} {last_name.upper()}. Como esta usted?'
print(greeting)

#adding whitespace with /n  and /t
print('Food:\nFavourites:\n\tJollof\n\tWaakye\n\tkenkey\nNon-Favourites:\n\tKokonte\n\tFufuu')
print('God caes for: \n\t1. My health \n\t2. My finances \n\t3. My Growth in Him \n')

#stripping whitespace with rstrip(), lstrip(), strip()

fav_lang  = ' French'
print(fav_lang.lstrip())

fav_lang = ' German '
print(fav_lang.strip())

fav_lang = 'latin '
print(fav_lang.rstrip())

#try it myself
first_ = 'Peter'
middle_ = 'Kobina'
last_ = 'Ntiforo'
f_name = f'{first_} {middle_} {last_}'
message_ = f'Hello {f_name}. Welcome Back to your Python lesson.' 
print(f"{message_} Let's begin, shall we?")

_1first = 'averly'
_2last = 'morillo'
full_ = f'{_2last} {_1first}'
print(full_.upper())
print(full_.lower())
print(full_.title())

print('The Lord once said, "Behold, I am the Lord, the God of all flesh. Is there anything too hard for me?"')

famous_person = 'Yahweh'
_message = f'{famous_person} said, "I have plans for you."'
print(_message)

_name = '\t Zaphenath\n\t-Paneah\t  '
print(_name.lstrip())
print(_name.rstrip())
print(_name.strip())