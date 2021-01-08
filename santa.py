import random

def hasSame(a, b):
	for i in range(len(a)):
		if a[i] == b[i]:
			return True
	return False

def includedBlackList(people, match, blacklist):
	for i in range(len(people)):
		if match[i] in blacklist[people[i]]:
			return True
	return False

# Assume correct usage
numPeople = int(input("How many people are doing secret santa?\n"))
if numPeople == 1:
	print("You can't do secret santa by yourself :(.")
	exit(-1)
print("We have {} people. Now enter their names and their blacklist.".format(numPeople))
print("The format is 'Name1: BlacklistedName1, ..., BlacklistedNameN'")
people = []
blacklist = {}
for _ in range(numPeople):
	input_ = input()
	if ":" in input_:
		name, blacklistString = map(lambda x: x.strip(), input_.split(":"))
	else:
		name = input_.strip()
		blacklistString = None

	if name in people:
		print("{} is already in our list!".format(name))
		exit(-1)
	people.append(name)

	if blacklistString is not None:
		blacklistNames = map(lambda x: x.strip(), blacklistString.split(","))
	else:
		blacklistNames = []
	blacklist[name] = set(blacklistNames)

print(people, blacklist)

match = people[:] # make shallow copy

while hasSame(people, match) or includedBlackList(people, match, blacklist):
	random.shuffle(match)

for i in range(len(people)):
	from_name = people[i]
	to_name = match[i]
	f = open("{}.txt".format(from_name), "w+")
	f.write("Hello {}, you are giving a present to {}!\n".format(from_name, to_name))
	f.close()

print("Have fun with Secret Santa! :)")
