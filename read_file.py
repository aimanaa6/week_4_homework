text = open("/Users/maratdavudov/PycharmProjects/Exercise13/pelican3.txt").read()
print(type(text))
print(text)
pelican_list = []
pelican_list=open("/Users/maratdavudov/PycharmProjects/Exercise13/pelican3.txt", "r").read().splitlines()
print(pelican_list)
print(len(pelican_list))

for line in open("/Users/maratdavudov/PycharmProjects/Exercise13/pelican3.txt", "r"):
    print(line)
