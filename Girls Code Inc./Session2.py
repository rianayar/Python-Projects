# # inputs
# print("What is your name?")
# name = input()
# print("Hello", name)
# print()

# # COMMENT ABOVE CODE BEFORE CONTINUING

# # Conditionals: if, elif, else 
# x = 15
# y = -8
# if(x > y):
#   print("x is greater than y")
# elif(x == y):
#   print("x is equal to y")
# else:
#   print("x is less than y") 
# # using the same x and y we can check conditions on the same line 
# if x < 0 and y < 0:
#   print("both number are negative") 
# elif x < 0 or y < 0:
#   print("one number is negative") 
# else:
#   print("both numbers are positive") 

# print()
# # COMMENT ABOVE CODE BEFORE CONTINUING 

# Lists
# List of Strings 
movies = ["Frozen", "Harry Potter", "Moana"]
print(movies)
#!! Indexing starts from 0 !!
print(movies[0])
print(movies[1])
print(movies[2])
print(movies[-1])
# Modify the list 
movies[2] = "Lion King"
print(movies)
# Append and Insert 
movies.append("Matilda")
print(movies)
movies.insert(2, "Hidden Figures")
print(movies)
# Slicing the list 
print(movies[0:2])
# Removing an item 
movies.remove("Matilda")
print(movies)
# Remove with pop: removes and stores the data 
currentMovie = movies.pop(0)
print(movies)
print(currentMovie)
# Combining lists 
friendsMovies = ["Soul Surfer", "Coco", "Alladin"]
movies.extend(friendsMovies)
print(movies)
# Length of a list 
numMovies = len(movies)
print("Number of movies in the list: ", numMovies)

# # COMMENT ABOVE CODE BEFORE CONTINUING 

# print()
# # List of ints
# numbers = [12, 8, 20, 54, 67, 50]
# print(numbers)
# # store a sorted list in numbersSorted
# numbersSorted = sorted(numbers)
# print("New Sorted List: ", numbersSorted)
# print("Original List: ", numbers)
#   # sort the original list 
# numbers.sort()
# print(numbers)
# # Reverse the order 
# numbers.reverse()
# print(numbers)