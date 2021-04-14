import random

compliments = ["You're Awesome!", "I think you are great!", "Keep being you!"]

wantsCompliment = input("Would you like to be complimented? Please type 'T' or 'F' \n")

if wantsCompliment == 'T':
  print(compliments[random.randint(0,len(compliments)-1)])
else:
  print('You chose not to be complimented.')