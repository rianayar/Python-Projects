# A7 - COP 1030 - Ria Nayar

import string

length = 0

cr = open("cr.txt", "rt")

# Remove punctuation
text = cr.read()
words = text.split()
table = str.maketrans("", "", string.punctuation)
stripped = [w.translate(table) for w in words]
assembled = " ".join(stripped)

# Print the number of words in the text file
print('Number of words in text file: ', len(words))

# Calculate and print the total word length
for word in words:
    length = length + len(word)
print("Total word length: ", length)

# Calculate the average word length
avgWordLength = length / len(words)
print("Average word length: ", avgWordLength)
