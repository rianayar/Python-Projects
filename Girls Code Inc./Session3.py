#FOR LOOPS AND WHILE LOOPS

#🚨 For Loops 🚨
print('For Loops Practice')
print()

numbers = [3, 2, 6, 7, 4]
#⭐️ Create a loop that iterates through the list above: ⭐️
for x in numbers:
	print(x+5)

print()

#💥 Create a loop iterating through a word: 💥
n = 1
for c in 'PYTHON':
	print('Letter', n, 'is', c)
	n = n + 1

print()

#🌸 Use the range() function in a for loop: 🌸
for y in range(5):
	print('y is', y)

print()

#🌼 Use the range() function with two arguments: 🌼
for number in range(3, 6):
	print('Number is', number)

print()

#🌺 Use the range() function with three arguments: 🌺
for a in range(1, 7, 2):
 	print('a is', a)

print()
print()

#🚨 WHILE LOOPS 🚨
print('While Loops Practice:')
print()

x = 12
#🍉 Create a while loop that subtracts 1 from x until x reaches 7 🍉
while x>7:
	print(x)
	x = x-1

print()

#🍓 Create a while loop that adds 1 to a number while it is less than 4 using a boolean variable 🍓
lessThanFour = True
n = 1
while lessThanFour:
	print(n)
	n = n + 1
	if n >= 4:
		lessThanFour = False