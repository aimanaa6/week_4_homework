import random
# imports module of code
# help(random)

lottery_numbers = random.sample(range(1,51),6)
# variable is lottery_numbers
# range is between integers, 1 to 51 (end value +1) otherwise end value is excluded
# random.sample is a function for sequences -  returns a list of unique elements chosen by population sequence
# random.sample = (population,k)
# a part of the random module
# returns a new list, leaving original population unchanged
# k = length of list
# list keeps the same order - can also be sorted and is a more flexible data structure (mutable)
# allows multiple data items to be extracted

print(lottery_numbers)
print(type(lottery_numbers))
# a list

print("Your lottery numbers are:", lottery_numbers)
# print a string and the output to the lottery_numbers variable
