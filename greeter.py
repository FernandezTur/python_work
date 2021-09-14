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
