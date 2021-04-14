# A2 for Week 3
# COP 1030 - 48320
# Ria Nayar - 1091791

# Get weight of first xenomorph from user input
print("Enter weight in kilograms of the first xenomorph")
weight1 = int(input())

# Get weight of second xenomorph from user input
print("\nEnter weight in kilograms of the second xenomorph")
weight2 = int(input())

# Get weight of third xenomorph from user input
print("\nEnter weight in kilograms of the third xenomorph")
weight3 = int(input())

# Calculate average using operations and round function and print output
avg = round((weight1 + weight2 + weight3)/3, 3)
print("\nThe average weight of the three xenomorphs is", avg, "kilograms")

