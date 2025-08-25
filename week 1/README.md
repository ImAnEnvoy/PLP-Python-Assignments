# PLP-Python-Assignment-Week1

## Description
This script takes two numerical inputs from the user and an operator (+, -, *, /) to perform a calculation. It then displays the result in a clear format.

## Objective
Practice creating Python programs to perform arithmetic and string, experimenting with variables, and exploring data types.

## Features
Accepts floating-point and integer inputs

#### Supports four arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

## Usage
#### Run the script:
python calculator.py

### Sample Interaction:

Enter first number: 10

Enter second number: 5

Choose operator (+,-,*,/): *

10.0 * 5.0 = 50.0

## Code Overview

first_num = float(input("Enter first number: "))

second_num = float(input("Enter second number: "))

operator = input("Choose operator (+,-,*,/)")

## Python Code
```
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
  `
  ```
## Note
No error handling for division by zero is currently implemented.
If an invalid operator is entered, the script will notify the user but may still attempt to print the result, which could raise an error.
