# numerical analysis
# using the range() fxn

for value in range(1, 6):
    print(value)

for num in range(6):
    print(num)

# making a list of numbers using list() and range()
numberss = list(range(1, 6))
print(numberss)

#printing a list of even numbers between 1 and 11
_even = list(range(2, 11, 2))
print(_even)

#...and odd numbers
_odd = list(range(1, 11, 2))
print(_odd)

#...1st 10 perfect squares
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

#statistics made simple
digits = [1, 2, 3, 4, 5, 23, 56, 780]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension...a simpler way of doing 'squares' exercise
squares = [value**2 for value in range(1, 11)]
print(squares)

#tryItYourself

for num in range(1, 21):
    print(num)

_num = list(range(1, 10000001))
print(_num)
print(min(_num))
print(max(_num))
print(sum(_num))

evenn = list(range(1, 20, 2))
print(evenn)

threes = list(range(3, 31, 3))
print(threes)

cubez = []
for cube in list(range(1, 11)):
    cubez.append(cube ** 3)
    print(cubez)

cubezz = [cube**3 for cube in range(1, 11)]
print(cubezz)



