# Testing if-elif-else chain
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

# Here is a better way of writing this
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")

# Using multiple elif blocks
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("Your admission cost is $" + str(price) + ".")

# Omitting the else block
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print("Your admission cost is $" + str(price) + ".")
