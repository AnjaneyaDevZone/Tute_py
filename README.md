
###Assignment 1

### greet.py
 #Personlised greeting

#Input from the user

name = input("Enter your name: ")
last_name = input("Enter your Last name: ")

# Greeting

print("Hello, " + name + " " + last_name + "! Welcome to the Python Program")

# math_Ops.py
Performs addition, subtraction, multiplication, and division on two numbers.
# Add two Numbers

Num1= int(input("Enter the first number: "))
Num2= int(input("Enter the second number: "))

Sum= Num1 + Num2

print("The sum of two numbers is: ", Sum)

# subtract two numbers

print("# subtraction")

Subtract= Num1 - Num2
print("The difference of two numbers is: ", Subtract)

# multiply two numbers
print("# multiplication")

multiply= Num1 * Num2
print("The product of two numbers is: ", multiply)

# divide two numbers
print("# division")

divide= Num1 / Num2
print("The quotient of two numbers is: ", divide)

# Assignment 2

### task_1.py
Checks whether the input number is even or odd.
#if a Number is Even or Odd

num= int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even: ", num)
else:
    print("The number is odd: ", num)


### task_2.py
Calculates the sum of integers from 1 to 50 using a loop.
# Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1, 51):
    sum += i

    print ("The sum of nnumbers from 1 to 50 is: ", sum)
    