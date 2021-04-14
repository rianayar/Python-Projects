# A5 for Week 6
# COP 1030 - 48320
# Ria Nayar - 1091791

# Function that returns my last name, no parameters
def yourLastName() :
  LAST_NAME = "Nayar"
  return LAST_NAME

# Function that returns 5 times the input parameter m
def fivester(m) :
  product = m * 5
  return product

# Function that returns if someone is old enough to play Minecraft based on input parameter age.
def oldEnoughToPlayMinecraft(age) :
  MIN_AGE = 7
  if age >= MIN_AGE:
    return True
  else :
    return False

def main() :
  print("Your Last Name Function Output:")
  print(yourLastName())
  print("Fivester Function Output:")
  print(fivester(5))
  print("Old Enough to Play Minecraft Output:")
  print(oldEnoughToPlayMinecraft(17))

main()
