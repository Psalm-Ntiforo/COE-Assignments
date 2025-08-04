# working with chunks of contents in a list. Note: The numbers used are the indices of the elements

floors = ['beverly hills', 'octosummit', 'ahenfie', 'phido dido 7', 'new jack city', 'city of elms']
print(floors)
print(floors[0:3])
print(floors[1:4])
print(floors[2:4])
print(floors[:2])  #automatically calls from the first, then the 2nd. THe calling stops at a value befor the actual index typed. So 0:4 will call index 0, 1, 2, 3.
print(floors[2:])
print(floors)
print(floors[0:5:2]) #introducing a last value tells python the number of names to skip in order to call out a desired set of values.


#loops in Slices
MI_mates = ['patrick', 'tilly', 'korkor', 'lukeman', 'daniel', 'bouncy',  'abena']
print(MI_mates)
print("Here are Aisha's favourite people:")
for mate in MI_mates[:4]:
    print(mate.title())

print("Here are Aisha's study cronies:")
for mate in MI_mates[:5]:
    print(mate.title())

print("This is Aisha's bestie:")
for mate in MI_mates[0]:
    print(mate.title())
#why did the output produce the extended spelling of his name?

#copying lists
conti_floors = floors[:]

floors.append('silicon valley')
conti_floors.append('akwaaba')

print("The floors in my hall include:")
print(floors)

print("Interestingly, the name of my hall is Conti :D. So Conti's floors include;")
print(conti_floors)

#this doesn't work as we want it to
conti_floors = floors
print(conti_floors)
print(floors) 


#tryityourself
#using the MI_mates list...
print(MI_mates)
print("The 1st 3 items in the list are:")
print(MI_mates[:3])
print("3 items from the middle of the list include:")
print(MI_mates[2:5])
print("The last three items in the list are:")
print(MI_mates[-3:])

books = ['Beautiful Ones are not yet born', 'sea of trolls', 'the treasure hunt', 'sintim', 'oliver twist', 'Tell my son to hold on to his gun']
aisha = books[:]
books.append('Suspect')
aisha.append('Caapito Messed up')

print(books)
print(aisha)
print("My fav books are:")
print(books[0:7:2])
print("Aisha's fav books are:")
print(aisha[0:7:2])


