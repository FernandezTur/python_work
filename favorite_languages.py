# A dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# Simple value read and print
print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")

# Now looping through all the values.
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title())

# Looping through all the keys in a dictionary
for name in favorite_languages.keys():
	print(name.title())

# Looping through the keys is the default behavior
# when looping through a dictionary. This could be written as:
for name in favorite_languages:
	print(name.title())

# Access the value associated with any key inside the loop
# using the current key. Example below...
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("  Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")

