def count(string, character):
	count = 0
	for letter in string:
		if letter == character:
			count = count + 1
	return count	

count_a = count("banana", "a")
print 'There are ', count_a, 'letter a in the word banana'

