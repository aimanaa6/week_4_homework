cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese is a list that is mutable
# contains three substrings already

# cheese += 'Oke'
# treats the string as separate characters
# output value is 'O','k','e'
# need to put brackets around ['Oke']

# print(cheese)

cheese += ['Oke']
# += is an augmented assignment operator - assigns value to the variable
# [] are required so 'Oke' is treated as a single element
# adds on to the right of the list

print(cheese)

# adding two values

cheese.extend(['Feta', 'Brie'])
# method (.extend) only takes one argument
# [] one argument containing list values

print(cheese)