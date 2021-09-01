squares = []
for value in range(1,11):
		square = value**2
		squares.append(square)
		
print(squares)

#A more concise version of the code is to omit the square variable:
squares = []
for value in range(1,11):
		squares.append(value**2)

print(squares)

#Now using a list comprehension:
squares = [value**2 for value in range(1,11)]
print(squares)
