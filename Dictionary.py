# A8 - COP 1030-48320
# Ria Nayar

# Creating 2 lists from the .txt file
countries = ["Qatar", "Luxembourg", "Macau", "Lichtenstein", "Singapore", "Bermuda", "IsleofMan", "Brunei", "Monaco", "Kuwait", "Ireland", "Norway", "UnitedArabEmirates", "SintMaarten", "SanMarino", "Switzerland", "HongKong", "UnitedStates", "Jersey", "FalklandIslands"]
perCapita = [129700, 102000, 96100, 89400, 87100, 85700, 83100, 79700, 78700, 71300, 69400, 69300, 67700, 66800, 65300, 59400, 58100, 57300, 57000, 55400]

# Turning those 2 lists into 1 dictionary
dictionary = {countries[i]: perCapita[i] for i in range(len(countries))}

# Printing the Entire Dictionary as a table
print("Country\t\t\t\t|\tIncome")
print("----------------------------------")
for i in dictionary :
  print("{:17}\t|\t$ {}".format(i, dictionary[i]))

# Getting user input for country to find income
# Using while loop to repeat the search in case of spelling mistakes
while True:
  val = input("\n\nEnter the country name with no spaces: ")

  if val in dictionary :
    print("The per capita income of", val, "is: $", dictionary[val])
  else :
    print("The country you entered is not part of our dictionary.\nPlease check spelling and continue to try again")

  state = input("\n\nIf you would like to repeat the search, type Y. Else, type N: ")
  if state == 'N':
    break
