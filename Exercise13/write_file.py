file = open('pelican.txt', 'a')
# opened file 'pelican.text' to append mode (add)
# new context can be added rather than overwriting

first_line = file.write("A wonderful bird is the pelican\n")
# the method .write writes the first line of text to the file (string)

second_line = file.write("His bill holds more than his belican\n")

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
# list of lines
# \n is added to each element create a new line

file.writelines(lines)
# method .writelines adds the sequence of strings to a file
# takes multiple strings and adds them at once
# must add \n - won't automatically be a new line