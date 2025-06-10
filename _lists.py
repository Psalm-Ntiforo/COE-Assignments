# lists
ntiforos = ['Peter', 'Etor', 'Psalm', 'Max', 'Leo', 'GrandPops', 'GrandMa', 'Ellis', 'Penory', 'Reese', 'Jane']
print(ntiforos)
print(ntiforos[0])
print(ntiforos[2].upper)
print(ntiforos[6])
print(ntiforos[-1])
print(ntiforos[-2])

message = f'Hola, {ntiforos[0]}'
print(message)

message = f'Hola, {ntiforos[1]}'
print(message)

message = f'Hola, {ntiforos[2]}'
print(message)

message = f'Hola, {ntiforos[3]}'
print(message)

message = f'Hola, {ntiforos[4]}'
print(message)

message = f'Hola, {ntiforos[5]}'
print(message)

message = f'Hola, {ntiforos[6]}'
print(message)

message = f'Hola, {ntiforos[7]}'
print(message)

_cars = ['audi', 'bentley', 'toyota', 'mitsibitsi', 'beamer', 'mercedes', 'maserati']

_messsage = f'In the near future, I would love to own my own {_cars[0]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[1]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[2]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[3]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[4]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[5]} SUV.'
print(_messsage)

_messsage = f'In the near future, I would love to own my own {_cars[6]} SUV.'
print(_messsage)

# changing elements in a list
_cars[2] = 'Tesla'
print(_cars)

_cars[3] = 'Lexus'
print(_cars)

# adding elements to the end of lists
_cars.append('kantanka')
_cars.append('chevvy')
_cars.append('citroen')
print(_cars)

_cars.insert(0, 'ferari')
_cars.insert(5, 'quadbike')

print(_cars)

del _cars[5]
del _cars[0]
_cars.remove('bentley')
print(_cars)

pop_car = _cars.pop()
popp_car = _cars.pop(6)
print(_cars)
print(pop_car)
print(f"{pop_car.title()} is Mother's fav SuV!")
print(f"{popp_car.title()} is Leo's company")


# exercise
_guests = ['Kwaku', 'Edmund', 'Copson', 'Bernice', 'Daniel', 'Speed']
_message = f'Hi, {_guests[0]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[1]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[2]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[3]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[4]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[5]}. I cordially invite you to dinner at my place.'
print(_message)

print(_guests[0])
_guests[0] = 'Kwame'
_message = f'Hi, {_guests[0]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[1]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[2]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[3]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[4]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[5]}. I cordially invite you to dinner at my place.'
print(_message)

print(f"Guys! I've got a better venue with larger tables!")

_guests.insert(0, 'Mavis')
_guests.insert(4, 'Aisha')
_guests.append('Nissi')
print(_guests)

_message = f'Hi, {_guests[0]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[1]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[2]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[3]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[4]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[5]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[6]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[7]}. I cordially invite you to dinner at my place.'
print(_message)
_message = f'Hi, {_guests[8]}. I cordially invite you to dinner at my place.'
print(_message)

# sorting lists

men_of_God = ['abraham', 'joshua', 'moses', 'hosea', 'david']
men_of_God.sort()
print(men_of_God)
men_of_God.sort(reverse=True)
print(men_of_God)



