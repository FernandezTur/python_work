#Example of tuples. These are immutable lists. meaning that they can't change.
dimensions = (200, 50)

#Changing the value of a tuple returns in error
#dimensions[0] = 250

print(dimensions[0])
print(dimensions[1])

#Looping through a tuple is ok
for dimension in dimensions:
	print(dimension)

#overwriting a variable is ok. So replacing a tuple with another works.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
