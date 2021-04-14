#Introduction To Functions in Python

#🚨 CREATE THREE FUNCTIONS: 🚨
#⭐️ Create a function that prints 3 sentences ⭐️
def printHello():
	print('Hello!')
	print('I like coding!')
	print('Have a nice day!')

#⭐️ Create a function that squares a number ⭐️
def square(x):
	y = x * x
	return y

#⭐️ Create a function that adds two numbers ⭐️
def add(x, y):
	return x + y

#🚨 CALL YOUR FUNCTIONS HERE: 🚨
#🌻 Call the function that prints 3 sentences: 🌻
printHello()

print()
print('Input a number to Square: ')
n = int(input())
#🌻 Square the user's input using a function: 🌻
print('The square is: ', square(n))

print()
a = 5
b = 18
#🌻 Add a and b using the function you created: 🌻
sum = add(a, b)
print('The sum is: ', sum)