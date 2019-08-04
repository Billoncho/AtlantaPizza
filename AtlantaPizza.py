# AtlantaPizza.py
# Billy Ridgeway
# Asks the user how many pizzas they would like to order.
# Asks how much it is on the menu and then calculates the
# sales tax and total amount due.

# Ask the person how many pizzas they want.
n = eval(input("How many pizzas would you like to order: "))

# Ask for the menu cost of each pizza.
cost = eval(input("What is the menu prize of the pizza: "))

# Calculate the total cost of the pizzas as our subtotal.
tc = cost * n

# Calculate the sales tax owed, at 8% of the subtotal.
st = tc * .08

# Add the sales tax to the subtotal for the final total.
ft = tc + st

# Show the user the total amount due, including tax.
print("The price of your pizzas is $", tc, "and $", st, "is state sales tax.")
print("Your order comes to a total of $", ft, "including tax.")
