# A4 for Week 5
# COP 1030 - 48320
# Ria Nayar - 1091791

iterate = 0
first = "Ria"
last = "Nayar"
length = len(first + last)
numList = []

print("Hi " + first, last + "! You're looking amazing today <|:0}")

while iterate < length:
  num = int(input("Enter a number\n"))
  numList.append(num)
  iterate = iterate + 1

for i in range(0, len(numList)): 
    numList[i] = int(numList[i])

numList.sort()
print("There were", len(numList), "numbers entered .")
print("The sum of the numbers entered is ", (sum(numList)),  ".")
print("The average of the numbers entered is ", sum(numList)/len(numList),  ".")
print("The largest of the entered values is ", numList[7], ".")
print("The smallest of the entered values is ", numList[0], ".")
