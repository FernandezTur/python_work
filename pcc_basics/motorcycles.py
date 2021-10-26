#Changing, adding, and removing elements from a list
motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles)

#modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to a list
motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Now starting from an empty list
print("\nNow starting from an empty list...")
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('susuki')

print(motorcycles)

#Inserting elements to a list
print("\nNow inserting an element...")
motorcycles.insert(0, 'ducati')

print(motorcycles)

#Removing an element/item from list with del
del motorcycles[0]
del motorcycles[1]

print(motorcycles)

#Using the pop method
print("\nUsing the pop method")

motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'susuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'susuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#Remove value from list
motorcycles = ['honda', 'yamaha', 'susuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#Work with value (similar to pop??)
motorcycles = ['honda', 'yamaha', 'susuki', 'ducati']
print(motorcycles)

most_expensive = 'ducati'
motorcycles.remove(most_expensive)
print(motorcycles)
print("\nA " + most_expensive + " is too expensive for me.")
