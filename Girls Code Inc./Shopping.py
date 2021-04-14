# Starter Template for Shopping
# Mix it up and enjoy :)

#🚨🚨 Create your functions below:🚨🚨
#⭐️ Name and create a  function that returns the money left after buying this item. ⭐️
def moneyLeft(budget, price):
	return budget - price

# ⭐️ Name and create a unique function to calculate the amount of tax to be added added on an item. ⭐️
def getTax(percent, price):
	return percent * price/100

#⭐️ Name and create a unique function to see if you can purchase an object based on your budget. ⭐️
# Hint: use an if-else statement.
def haveEnoughMoney(budget, price):
	if (budget - price) >= 0:
		return True
	else:
		return False

#⭐️ Name and create a unique function to find out what percent of your budget is being used to buy that one item. ⭐️
def percentOfBudget(budget, price):
	return price/budget * 100

#🚨🚨 Test your functions in this section: 🚨🚨
print('What is your budget?')
budget = float(input())
print('What is the price of the item?')
price = float(input())
print('What is the percent tax?')
tax = float(input())
print()

#🌸 Create a variable that calls the tax function and adds it to the price to get the price with tax: 🌸
priceWithTax = price + getTax(tax, price)
#🌸 Print out the price with tax: 🌸
print('The price with tax is: ', priceWithTax)

#🌺 If they have enough money to buy the item, print that they have enough, how much money they will have left, and the percent of their budget it takes up. 🌺
#HINT: use an "if" conditional, and calculate using price with tax
if(haveEnoughMoney(budget, price)):
	print('You have enough money to buy this.')
	print('You will have $', moneyLeft(budget, priceWithTax), 'left')
	print('It will take up', percentOfBudget(budget, priceWithTax), 'percent of your budget')

#🌺 If they don't have enough money, print that the item is not within the budget. 🌺
#HINT: use an else conditional
else:
	print('This item is not within your budget')
