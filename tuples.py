#an immutable(unchangeable) list is called a tuple.
bufffet = ('fried rice', 'jollof', 'kenkey', 'salad', 'lemonade')
for food in bufffet:
    print(food)
    
#the values n tuples cannot be replaced. so the code below won't run
#food[2] = 'fufu'
#print(food)

#to make changes, you'd have to define the same variable again, make the changes in in before you print or execute.
bufffet = ('fried rice', 'jollof', 'banku', 'salad', 'lemonade', 'lentil soup')
for food in bufffet:
    print(food)
    