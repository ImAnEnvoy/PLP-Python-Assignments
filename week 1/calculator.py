first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operator = input("Choose operator (+,-,*,/)")

if(operator == '+'):
    result = first_num + second_num
elif(operator == '-'):
    result = first_num - second_num
elif(operator == '*'):
    result = first_num * second_num
elif(operator == '/'):
    result = first_num / second_num
else:
    print("operator not recognize")

print(f"{first_num} {operator} {second_num} = {result}")