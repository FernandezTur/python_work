#This program shows how to sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print('\nRemember that "sort" changes the list permamnently...\n')
#Note that sorting changes the list permanently...

#Sorting in reverse (Make sure the "True" is capitalized)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Temporarirly sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Printing the list in reverse order

print("\nPrinting the cars in reverse now...\n")
cars.reverse()
print(cars)

#Note this method is also permanent
print("Note the reversal is permanent.")

#Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']

list_length = len(cars)
print("\nThe length of the list is:" + str(list_length))


#Examples for if statements
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
