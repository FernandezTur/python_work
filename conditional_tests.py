#Practice conditional testing

#Test 1: Equality
print("Test #1")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#Test 2: lower() function. This functions produces lower cases
print("\nTest #2")

car = 'Subaru'
print("Is car == 'Subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car == 'Audi'? I predict False.")
print(car.lower() == 'audi')

#Test 3: Greater than or equal
print("\nTest #3")
age_0 = 2
age_1 = 3
age_2 = 2

print("Is " + str(age_0) + " lower than " + str(age_1) + "?")
print(age_0 <= age_1)

print("Is " + str(age_0) + " greater than " + str(age_1) + "?")
print(age_0 >= age_1)

print("Is " + str(age_0) + " equal to " + str(age_1) + "?")
print(age_0 == age_1)

print("Is " + str(age_0) + " equal to " + str(age_2) + "?")
print(age_0 == age_2)

#Test 4: keywords 'and' and 'or'
print("\nTest #4")
age_0 = 2
age_1 = 3
age_2 = 2

print((age_0 >= age_1) and (age_0 <= age_2))
print((age_0 >= age_2) and (age_1 <= age_2))
print((age_0 >= age_1) or (age_0 <= age_1))
print((age_0 >= age_2) or (age_1 <= age_2))
#Test 5
print("\nTest #5")
