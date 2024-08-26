                                 # CALCULATOR
#function adds two numbers
def add(x, y):
   return x + y
#function subtracts two numbers
def subtract(x, y):
   return x - y
#function multiplies two numbers
def multiply(x, y):
   return x * y
#function divides two numbers
def divide(x, y):
   if y == 0:
      return "Error! Division by zero is not allowed."
   else:
      return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# user to input an operation choice
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

# calculation based on the user's choice
if choice == '1':
   print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
   print(num1, "/", num2, "=", divide(num1, num2))

else:
   print("Invalid input")