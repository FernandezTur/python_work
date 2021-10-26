## Removing all instances of specific values from a list
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

## Positional arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

## Multiple function calls
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

## Order matters in positional arguments
describe_pet('harry', 'hamster')

## Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

## Default values
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
