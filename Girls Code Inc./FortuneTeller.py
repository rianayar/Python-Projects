fortunes = ['You will have an exciting adventure!','You will be successful!','You will enjoy a relaxing vacation','You will live a long and happy life','You will accomplish great things','You will grow up to be very wise','You will always be loved','You will have many friends']

# pull blue and red apart first 
def firstQuestion(color):
  if color.lower() == 'blue' or color.lower() == 'yellow':
    return input("Pick a number: Type '1','4','3', or '6'\n")
  else:
    return input("Pick a number: Type '2','5','7' or '8'\n")

def secondQuestion(number):
  # if the number chosen is odd then it will go to the other set of 4 number options
  # if the number is even, then it will go to the same set of 4 number options
  if number == 1 or number == 3 or number == 8 or number == 2:
    return input("Pick a number: Type '2','5','7' or '8'\n")
  else:
    return input("Pick a number: Type '1','3','4', or '6'\n")

def getFortune(finalNumber):
  # have to subtract 1 because indexing for our fortunes list starts at 0 (the first fortune is found at index 0)
  return fortunes[finalNumber-1]

print("Welcome to my Fortune Teller program!")
color = input("Pick a color: Type 'Blue', 'Red', 'Yellow', or 'Green'")
number = firstQuestion(color)
# have to use int() around the input to turn the string that the user gave into a number the computer can read
fortuneNumber = secondQuestion(int(number))
print(getFortune(int(fortuneNumber)))

# you can use your own fortune teller to check that your program works correctly!