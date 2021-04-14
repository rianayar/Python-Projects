name = input("What is your name? ")
age = input("What is your age? ")

# import random
# age = random.randint(10,14)

info = "Your name is {} and you are {} years old.".format(name, age)

print(info)
print('There are a total of ' + str(len(info)) + ' characters in the above sentence.')
print(info.lower())
print(info.upper())
print(info.split())