# Defining the function calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (price * discount_percent)/100
    else:
        return price

# calling the function and passing and assigning it to a variable "result"
result1 = calculate_discount(80,30) # when discount > 20
result2 = calculate_discount(70, 6) # when discount < 20


# Printing the result on the terminal
print(f"Final price: (discount > 20) ${result1}")
print(f"Final price (dicount < 20): ${result2}")