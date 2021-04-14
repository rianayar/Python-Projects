# Print Statements 
print("Hello World")
print("Girls Code!")

print()
# Variables and Data Types 
# Strings 
firstName = "Coder"
lastName = "Girl"
name = firstName + " " + lastName
print(name)
# integer and float 
x = 5
print(x + 2)
print(x + 2.5)
# boolean: returns true or false 
print(5 > 8)
print(20 < 30)
# casting: changes the data type a variable holds 
a = int(2.8) 
print(a)
b = float(4)
print(b)
s = str(a + b)
print(s)

print()
# Built in Functions 
# len(): returns the length of a string 
print(len("Teamwork")) 
print(len("Girl Power"))
# .lower(): turns all uppercase letters into lowercase 
string = "Girl Power"
print(string.lower())
# .upper(): turns all lower case letters into uppercase
message = "i am a coder"
print(message.upper())
# format(): substitute values into your code 
print("I am learning to code in {}".format("Python")) 
print("I am {} year old".format(17))
# max() and min()
print(max(1, -2, 85,)) 
print(min(1, -2, 85,)) 
# abs()
print(abs(-15))
# round()
print(round(5.5))
print(round(3.1))
# random() and randint()
import random
print(random.random()) # returns random decimal from 0-1
print(random.randint(1, 10)) # returns random integer from 1 to 10

print()
# Indexing and Slicing 
message = "Girls Code!"
print(message[0])
print(message[3])
print(message[0 : 4])
print(message[0 : 5])