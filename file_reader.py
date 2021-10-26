with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

# Use rstrip to remove the whitespace at the end (read function does that)
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# Read a file line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Making a list of lines from a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
