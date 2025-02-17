import random

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# treats it as a string and adds it letter by letter
cheese+= 'Oke'
# correct way to do it
cheese+= ["Oke"]
print(cheese)
cheese+=['Brie', 'Mimolette']
print(cheese)

# this is a string
tup='Hello'
# prints length of a string in characters
print(len(tup))
# this is a tuple
tup='Hello',
# prints length of a tuple which only has one element in it
print(len(tup))

lotto_numbers=[]
for i in range(6):
    random_number = random.randint(1, 50)
    lotto_numbers.append(random_number)
print(lotto_numbers)



