output = open('pelican3.txt', 'a')
text = output.write("A wonderful bird is the pelican\n")
text = output.write("His bill holds more than his beak\n")
list = ["He can take in his beak\n", "Enough food for a week\n", "But I'd be damned if I see how the helican\n"]
text = output.writelines(list)