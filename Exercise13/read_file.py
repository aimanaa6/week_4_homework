lines = open('sample/pelican.txt', 'r').read()
# open function returns a file stream
# .read() reads all the contents in the file and returns it as a single string
print(type(lines))
# type function - class is a string
print(lines)

lines_list = open('sample/pelican.txt', 'r').read().splitlines()
# .splitlines() splits a string into a list of lines
# breaks at every new line character
print(type(lines_list))
print(lines_list)

for line in (lines_list):
# for loop iterates through each line in list
# each iteration is assigned to variable 'line'
    print(line)