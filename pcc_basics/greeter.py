## Writing clear prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

## Defining a function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

## Passing information to a function
def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('jesse')

## Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")
	
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")
