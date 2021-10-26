#First count to twenty (20)
for value in range(1,21):
	print(value)

#List number from 1 to 1 million, then sum them.
million = []
for value in range(1,1000001):
	million.append(value)
#	print(value)
print("The minimum is " + str(min(million)) + ".\n")
print("The maximum is " + str(max(million)) + ".\n")
print("The sum is " + str(sum(million)) + ".\n")
