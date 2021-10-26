#Make a list of the multiples of 3 from 3 to 30.
#Usa a for loop to print the numbers in your list.

threes = []
for value in range(1,11):
	threes.append(value*3)

print(threes)

#Comprehensive method
threes = [value*3 for value in range(1,11)]
print(threes)
