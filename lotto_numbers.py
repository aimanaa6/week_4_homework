import random
lotto_numbers=[]
for i in range(6):
    random_number = random.randint(1, 50)
    lotto_numbers.append(random_number)
print(lotto_numbers)
