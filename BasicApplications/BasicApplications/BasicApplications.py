#print & type elements examinations
x = 7.125
print("x = ", x)
print(type(x), "\n")
x*2
print("x = ", x)
print(type(x), "\n")
x**3
print("x = ", x)
print(type(x), "\n")
x/4
print("x = ", x)
print(type(x), "\n")
x//7
print("x = ", x)
print(type(x), "\n")
x%5
print("x = ", x)
print(type(x), "\n")

x = "Hello World"
print("x is", x)
print(type(x))

#input
name = input("What is your name?\n Enter your name here: ")
print("username is: ", name)
print(type(name))

#integer inputs
num = int(input("Enter a number here: "))
print("number is: ", num)
print(type(num))

#float inputs
fnum = int(input("Enter a number here: "))
print("number is: ", fnum)
print(type(fnum))

#import libraries
import math
number = int(input("Enter a number here: "))
print("Square root of", number, " is: " , math.sqrt(number))
print("Power of", number, " is: " , math.pow(number))

#invoke library syntax
dir(math)

#evaluation method
variable1 = eval(input("Enter some expression: "))
print (variable1)

#basic circle area calculation application with evaluation method
radius = eval(input("Enter a radius for your circle: "))
area = radius*radius*math.pi
print("The radius of your circle is", radius, "and the area: ", area)

#switch variable
x, y = 20, 30
print(x,y)
x, y = y, x
print(x,y)

#constant value
#only express the variable with capital letters
PI = 3.149
print(PI)

#overloading variables
i = 10
i = i + 1
i += 5 #i = i + 5

2e3 #2*10^3
2e-1 #2*10^-1
31.9e3 #31.9*10^3

#average applications
x, y, z = eval(input("Enter 3 number here:"))
average = (x + y + z) / 3
print(average)

#seconds to minute application
second = eval(input("Enter an integer for seconds: "))
#Get minutes remaining seconds

minutes = seconds // 60
remainingSeconds = seconds % 60

print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")

#Tax amount application(tax = 0.06)
purchase = eval(input("Enter purchase amount here: "))
tax = purchase * 0.06 #or -> print(round(tax,2))
print("Tax is: ", (int)(tax*100/100.0))

#Boolean
print(7==4)
print(7!=4)
print(7>4)
print(7>=4)
print(7<4)

#Grade application (with if-else)
gradeValue = eval(input("Enter your grade here: "))
if gradeValue >=55:
    print("Passed")
else:
    print("Failed")

#number comparison
number1, number2 = int(input("Enter 2 number here to compare: "))
if number1 == number2:
    print(number1, " is equal to", number2)
elif number >= number2:
    print(number1, " >=", number2)
elif number1 <= number2:
    print(number1, " <= ", number2)

#Grade application 
grade = eval(input("Enter your grade here: "))
if grade >= 90:
    print("Your grade: A")
elif grade >=70:
    print("Your grade: B")
elif grade >=55:
    print("Your grade: C")
elif grade >=40:
    print("Your grade: D")
else:
    print("You failed")

