import random

def hasSame(a, b):
	for i in range(len(a)):
		if a[i] == b[i]:
			return True
	return False

people = ['Steven', 'Jeffrey', 'Lucy', 'Yuehan', 'Johnny', 'Delina', 'Jiashu', 'William']
match = ['Steven', 'Jeffrey', 'Lucy', 'Yuehan', 'Johnny', 'Delina', 'Jiashu', 'William']

while hasSame(people, match):
	random.shuffle(match)

for i in range(len(people)):
	from_name = people[i]
	to_name = match[i]
	f = open("{}.txt".format(from_name), "w+")
	f.write("Hello {}, you are giving a present to {}!".format(from_name, to_name))
	f.close()

print("Have fun with Secret Santa! :)")
