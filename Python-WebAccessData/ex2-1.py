import re

fh = open('regex_sum_221152.txt')

num_list = list()

for line in fh:
	line = line.rstrip()
	nums = re.findall('[0-9]+', line)
	if nums:
		for n in nums:
			num_list.append(int(n))
		
print(sum(num_list))
