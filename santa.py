import random

def hasSame(a, b):
	for i in range(len(a)):
		if a[i] == b[i]:
			return True
	return False

# Assume correct usage
numPeople = int(input("How many people are doing secret santa?\n"))
if numPeople == 1:
	print("You can't do secret santa by yourself :(.")
	exit(-1)
print("We have {} people. Now enter their names.".format(numPeople))
people = []
for _ in range(numPeople):
	while True:
		name = input()
		if name in people:
			print("{} is already in our list! Enter another name.".format(name))
			continue
		people.append(name)
		break
match = people[:] # make shallow copy

while hasSame(people, match):
	random.shuffle(match)

for i in range(len(people)):
	from_name = people[i]
	to_name = match[i]
	f = open("{}.txt".format(from_name), "w+")
	f.write("Hello {}, you are giving a present to {}!\n".format(from_name, to_name))
	f.close()

print("Have fun with Secret Santa! :)")
