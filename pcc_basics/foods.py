#Copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #using ":" tells it to slice the whole list

#This doesn't work. Example of why use slice to copy and not the list itself
#friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#Now use a for loop to print the list
print("\nMy favorite foods are:")
for value in range(0,len(my_foods)):
	print(my_foods[value])

print("\nMy friend's favorite foods are:")
for value in range(0,len(friend_foods)):
	print(friend_foods[value])
