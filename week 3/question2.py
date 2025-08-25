#------- Exercise 2-------------
# Defining the function calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (price * discount_percent)/100
    else:
        return price

# Prompt for user input
price = float(input("Enter a value for Price: "))
discount = float(input("Enter discount: "))

# calling the function and passing and assigning it to a variable "result"
result = calculate_discount(price, discount)

# Printing the result on the terminal
print(f"Final price: ${result}")