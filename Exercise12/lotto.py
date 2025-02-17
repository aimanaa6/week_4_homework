import random
# imports module of code
# help(random)

lottery_numbers = random.sample(range(1,51),6)
# variable is lottery_numbers
# range is between integers, 1 to 51 (end value +1) otherwise end value is excluded (counts up from zero)
# random.sample is a function for sequences -  returns a list of unique elements chosen by population sequence
# random.sample = (population,k)
# a part of the random module
# k = length of list

print(lottery_numbers)
# returns a new list, leaving original population unchanged
# list keeps the same order - can also be sorted and is a more flexible data structure (mutable)
# allows multiple data items to be extracted

print(type(lottery_numbers))
# a list

print("Your lottery numbers are:", lottery_numbers)
# print a string and the output to the lottery_numbers variable
