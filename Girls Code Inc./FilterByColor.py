# Finished Example for FilterByColor
# Remix this code and make it your own! Feel free to change variable and function names.

# List a few items and their colors (at least 4) within the brackets below
# Ex: 'pink flamingo'
objectsToFilter = ['pink flamingo', 'blue sky', 'red rose', 'red apple', 'green grass', 'blue shirt', 'pink dress', 'green leaves', 'red strawberry', 'green pear', 'blue umbrella', 'pink balloon']

# Add a line instructing the user what they need to type in
print('Choose a color:')
chosenColor = input('').lower()

# This is for the output
filteredList = []

# Below, create statements that check to see if the first word in the string obj matches the color we are filtering by. If they match, then that whole string is appended to the filteredList
# You can also do this with a for or a while loop
for x in objectsToFilter:
	if(x[0:len(chosenColor)] == chosenColor):
		filteredList.append(x)

# Below, create a print statement that tells what you were filtering by and then what colors are included.
# Ex: The pink objects include: ['pink flamingo', 'pink coat']
print('The', chosenColor, 'objects include:', filteredList)