# A3 for Week 4
# COP 1030 - 48320
# Ria Nayar - 1091791
print("Welcome to Ria's Eateria!\n")
name = input("What is your name?\n")
QUANTITY = int(input("How many pounds did you eat?\n"))

if QUANTITY <= 0:
  SUBTOTAL = 0
elif QUANTITY < 2 :
  SUBTOTAL = 17.99
elif QUANTITY >= 2 and QUANTITY <= 3.5 :
  SUBTOTAL = 24.99
elif QUANTITY > 3.5 and QUANTITY <= 7 :
  SUBTOTAL = 31.99
else :
  SUBTOTAL = 49.99

TAX_RATE = 0.0615
tax = round(SUBTOTAL * TAX_RATE, 2)
total = round(tax + SUBTOTAL, 2)

print()
print(name, "has eaten", QUANTITY, "pounds of food.")
print("Subtotal: $",SUBTOTAL)
print("Tax: $",tax)
print("The grand total is $",total)
