#print & type elements examinations
x = 7.125
print("x = ", x)
print(type(x), "\n")
x = x*2
print("x = ", x)
print(type(x), "\n")
x = x**3
print("x = ", x)
print(type(x), "\n")
x = x/4
print("x = ", x)
print(type(x), "\n")
x = x//7
print("x = ", x)
print(type(x), "\n")
x = x%5
print("x = ", x)
print(type(x), "\n")

x = "Hello World"
print("x is", x)
print(type(x))

#input
name = input("What is your name?\n\
Enter your name here: ")
# '\' conditional operator
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
from errno import EL
import math
from pickle import FALSE
from tkinter.font import ROMAN
number = int(input("Enter a number here: "))
print("Square root of", number, " is: " , math.sqrt(number))
print("Power of", number, " is: " , math.pow(number))
print("sin(PI/2) =", math.sin(math.pi))
print("Log(e) = ", math.log(math.e))

#or
from math import pow
print(pow(8,3))

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
seconds = eval(input("Enter an integer for seconds: "))
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


#Application: Compute Angle
x1, y1 = eval(input("Enter x, y coodinates of first angle: "))
x2, y2 = eval(input("Enter x, y coodinates of second angle: "))
x3, y3 = eval(input("Enter x, y coodinates of third angle: "))

a = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))

A = math.acos((c*c+b*b-a*a)/(2*b*c))
B = math.acos((math.pow(a,2)+math.pow(c,2)-math.pow(b,2))/(2*a*c))
C = math.acos((math.pow(a,2)+math.pow(b,2)-math.pow(b,2))/(2*a*b))

print("The tree angles are: ", (int) (A*100)/100.0 (int) (B*100)/100.0 (int) (C*100)/100.0 )

#Loops
for i in range(3):
    print("Hello", end= " ")

for i in range(2, 6, 2):
    j = input("enter a nunmber: ")
    print(j)

for character in "Programing Languages Concept" :
    print(character, end= " ")

#While loops
i = 0
while i < 10:
    print(i, end = " ")
    i = i + 1 #i += 1

#list
list(range(3, 15))
#=+5
list(range(3,15,5))

#Application: average of grades
totalGrades = 0
students = int(input("Enter here number of students in the class: "))
for x in range(students):
    print("Enter ", (x + 1), ". student grades here:")
    grades = eval(input(" "))
    totalGrades += grades

average = (totalGrades / students)

print("average of the class is: ", average)


#
print("?" * 3)

for i in range(4):
    print("*" * (i + 1))

#statistics librariy
import statistics

#invoke statistics library syntax
dir(statistics)

#Functions
print("max: ", max)
print("min: ", min)
print("sorting: ",sorted([45, 18, -2, -89], reverse = True))

#Prime number application
pnum = input("Enter a number here: ")
isPrime = True
if pnum == 1:
    isPrime = True
elif pnum > 1:
    for i in range(2, pnum):
        if(pnum % i ) == 0:
            isPrime = False
            break

if isPrime:
    print(pnum, "is a prime number")
else:
    print(pnum, "is not a prime number")


#EX2: Self-checkout machine
CENTS_PER_TOONÝE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTERS = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

cents = int(input("Enter number of cents: "))

print(cents // CENTS_PER_TOONÝE, "toonies")
cents = cents % CENTS_PER_TOONÝE
print(cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE
print(cents // CENTS_PER_QUARTERS, "quarters")
cents = cents % CENTS_PER_QUARTERS
print(cents // CENTS_PER_DIME, "dime")
cents = cents % CENTS_PER_DIME
print(cents // CENTS_PER_NICKEL, "nickel")
cents = cents % CENTS_PER_NICKEL

#EX3: The length of months
print("Callender of 2023")
monthInput = input("Enter the name of month: ")

days = 31

if monthInput == "April" or monthInput == "June" or monthInput == "September" or monthInput == "November":
    days = 30
elif monthInput == "February":
    days = "28 or 29"

print(monthInput, "has", days, "days in it.")

#EX4: triangle application
side1, side2, side3 = float(input("Enter three side of triangle here: "))

if side1 == side2 != side3 or side1 == side3 != side2:
    print("It's a isosceles.")
elif side1 == side2 == side3:
    print("It's a equilateral.")
elif side1 != side2 != side3:
    print("It's a scalene.")

#EXP5: Rating
RAISE_FACTOR = 2400
UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIUS = 0.6

rating = float(input("Enter the rating(0 - 0.4 - 0.6):"))

if rating == UNACCEPTABLE:
    performance = "UNACCEPTABLE"
elif rating == ACCEPTABLE:
    performance = ACCEPTABLE
elif rating == MERITORIUS:
    performance = MERITORIUS

if performance == "":
    print("That is not a valid rating.")
else:
    print("Based on that rating, the performance is %s"%performance)
    print("You will receive a raise of $%.2f"%(rating*RAISE_FACTOR))

#EXP6: Leap Years Application
year = int(input("Enter year here: "))

if year % 400 == 0:
    isLeapYear = True
elif year % 100 != 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True

if isLeapYear:
    print(year, " a leap year.")
else:
    print(year, " isn't a leap year")

#EXP7: Multiplication Table
print("    ", end="")
for i  in range(1, 11):
    print("%4d"%i, end = " " )
print()

for i  in range(1, 11):
    print("%4d"%i, end = " " )
    for j in range(1, 11):
        print("%4d"%(i * j) * 1, end = " " )
print()

#EXP8: Birthday calculater
day = 0 # birth day to be determined

question1 = "Is your birthday in Set1?\n" + \
    " 1  3  5  7\n" + \
    " 9 11 13 15\n" + \
    "17 19 21 23\n" + \
    "25 27 29 31" + \
    "\nEnter 0 for No and 1 for Yes: " 

answer = eval(input(question1))

if answer==1:

    day = day + 1


question2 = "Is your birthday in Set2?\n" + \
    " 2  3  6  7\n" + \
    "10 11 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31" + \
    "\nEnter 0 for No and 1 for Yes: " 

answer = eval(input(question2))

if answer==1:

    day = day + 2

question3 = "Is your birthday in Set3?\n" + \
    " 4  5  6  7\n" + \
    "12 13 14 15\n" + \
    "20 21 22 23\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: " 

answer = eval(input(question3))

if answer==1:

     day = day + 4
     
question4 = "Is your birthday in Set4?\n" + \
    " 8  9 10 11\n" + \
    "12 13 14 15\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: " 

answer = eval(input(question4))

if answer==1:

     day = day + 8
     
question5 = "Is your birthday in Set5?\n" + \
    "16 17 18 19\n" + \
    "20 21 22 23\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: " 

answer = eval(input(question5))

if answer==1:

     day = day + 16
     
print("\nYour birthday is "+ str(day) + "!")

#EXP9: Subtract random numbers application
#random number generate
import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)

#if num1 < num2 swap number1 with num2
if num2 > num1:
    num1, num2 = num2, num1

answer = eval(input("What is ", num1, " - ", num2 ))
result = num1 - num2
if answer == result:
    print("Your answer is correct")
else:
    print("your answer is wrong! ", num1, " - ", num2, " is: ", result)

#EXP10: Chinese Birth year sign
birthYear = eval(input("Enter your birth year here: "))
remaningYear = birthYear % 12

if remaningYear == 0:
    print("You born in Monkey year.")
elif remaningYear == 1:
    print("You born in Rooster year.")
elif remaningYear == 2:
    print("You born in Dog year.")
elif remaningYear == 3:
    print("You born in Pig year.")
elif remaningYear == 4:
    print("You born in Rat year.")
elif remaningYear == 5:
    print("You born in Ox year.")
elif remaningYear == 6:
    print("You born in Tiger year.")
elif remaningYear == 7:
    print("You born in Rabbit year.")
elif remaningYear == 8:
    print("You born in Dragon year.")
elif remaningYear == 9:
    print("You born in Snake year.")
elif remaningYear == 10:
    print("You born in Horse year.")
elif remaningYear == 11:
    print("You born in Sheep year.")
else:
    print("You enter a invalid year.")

#List in Python
c = [-31, 56, 5, 69, 215]
print(c)

print(c[0], c[1], c[2], c[3], c[4])
print(c[-1], c[-2], c[-3], c[-4], c[-5])

    #Lists are mutable objects: theirs elements can be modified
s = "hello"
print(s)
print(s[4], s[3], s[2], s[1], s[0])
print(len(s)) #Lenght of list
    #We can add 2 list 
b = [96, 45]
concatenatedList = b + c
print(concatenatedList)

for i in range(len(concatenatedList)):
    print(f'{i}: {concatenatedList[i]}')


#Tuples in Python
exampleIntTuple = (10,25,64)
exampleMixTuple = ("Anil", 1.5, -3, 45)

print(exampleIntTuple)
print(exampleMixTuple)

print(len(exampleIntTuple))
print(len(exampleMixTuple))

    #Tuples are inmutable: cant be modified
    #we can add 2 tuples

#Unpacking
studentTuple = ('Anil', 'Guvenc', [60, 55, 100])
studentName, studentSurname, studentGrade = studentTuple
print(studentName, studentSurname, studentGrade)

#EXP11: Lottery
import random
lottery = random.randint(0,99)
guess = eval(input("Enter your lottery number(pick two digits number)"))

#Gets digits of the lottery number 
lotteryDigits1 = lottery // 10
lotteryDigits2 = lottery % 10

#Get the digits of the users number
guessDigit1 = guess // 10
guessDigit2 = guess % 10

if guess == lottery:
    print("Exact match: you win $10000.")
elif (lotteryDigits1 == guessDigit2 and lotteryDigits2 == guessDigit1):
    print("Match all digits: you win $3000.")
elif(lotteryDigits1 == guessDigit1 or lotteryDigits2 == guessDigit2 or lotteryDigits1 == guessDigit2 or lotteryDigits2 == guessDigit1):
    print("Match one digit: you win $1000.")
else:
    print("Sorry no match.")

#EXP12: 
import random
#generate a random number to be guessed
number = random.randint(0,100)
print("Guess a magic number between 0 - 100")
guess = -1

while guess != number:
    
    guess = eval(input("Enter your guess: "))
    if guess==number:
        print("Yes, the generated number is",  number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

#Example: Create a primitive bar chart
numbers = [19,3,15,7,11]
for index, value in enumerate(numbers):
    print(f'{index:> 5}{value:>8} {"*" * value}')

colors = ['red', 'orange', 'yellow' ]
print(list(enumerate(colors)))
print(tuple(enumerate(colors)))
for index, value in enumerate(colors):
    print(f'{index}:    {value}')


numbers = [2,3,4,5,7,11,13,17,19]
print(numbers[6:len(numbers)])
print(numbers[6:])
print(numbers[:])
print(numbers[-1:-10:-1])
print(numbers[::-1])
numbers[-1]

numbers = [2,3,4,5,7,11,13,17,19]
numbers[0:3]
print(numbers)

#Sorting Numbers
numbers = [24,3,41,5,7,11,13,17,19]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

numbers.index(41)
    #Boolean type
print(1000 in numbers)
print(1000 not in numbers)

#Add list element
colors = ['red', 'orange', 'yellow' ]
colors.insert(0, 'pink')
print(colors)
colors.append('blue')
print(colors)
colors.extend(['green', 'gray'])
print(colors)

#list Comprenhensions
list2 = [item for item in range(1,6)]
print(list2)

list3 = [item for item in range(1,6)]
print(list3)
list3 = [pow(item,3) for item in range(1,6)]
print(list3)

#
colors_lower = ['red', 'orange', 'yellow']
color_capitals = [item.upper() for item in colors_lower]
print(color_capitals)

#
cubes = [(x, x**3) for x in range(1,6)]
print(cubes)

#Functions
age = [5,12,17,18,24,32]
def myFunc(x):
    if x <18:
        return False
    else:
        return True

adults = filter(myFunc, age)
print(type(adults))

for item in adults:
    print(item)

#Filter
randomList = [1,'a',0, False, True, '0']
filteredList = filter(none, randomList)
for items in filteredList:
    print(items)

#even or odd
numbers = [10,3,7,1,9,4,2,8,5,6]
def is_odd(x):
    return x % 2 != 0

filteredList = filter(is_odd, numbers)

for items in filteredList:
    print(items)

#list Comprehensions
numbers = [10,3,7,1,9,4,2,8,5,6]
[item for item in numbers if is_odd(item)]

#LAMBDA
object = lambda x: x % 2 != 0
print(object(10))

#Multiplication and summation in lambda
multiplication_object = lambda a,b: a * b
print(multiplication_object(3,5))

summation_object = lambda a,b,c : a+b+c
print(summation_object(5,3,9))

#List command
numbers = [10,3,7,1,9,4,2,8,5,6]
new_list = filter(lambda x: (x % 2 != 0), numbers)
print(list(new_list)) #Directly listed array. Don't have to use for loop.

#Map Functions
def myfunc(n):
    return len(n)

my_tuple = ('apple', 'banana', 'chery')

result = map(myfunc, my_tuple)
print(type(result)) #prints type of result object
print(list(result))

#Combine filter and Map functions
numbers = [10,3,7,1,9,4,2,8,5,6]
result = list(map(lambda x: x**3, filter(lambda x: x % 2 != 0, numbers)))

print(result)

#Combine with for loop
numbers = [10,3,7,1,9,4,2,8,5,6]
result = [item **3 for item in numbers if item % 2 != 0]
print(result)

#Create a list with range
my_list = list(range(1,16))
  #get just the even numbers from my_list
is_even = filter(lambda x: (x % 2 == 0), my_list)
  #use map and filter methods to map just the even numbers to their squares
result = list(map(lambda x: x**2, is_even))

print(my_list)
print(is_even)
print(result)

#Exp: Map a list of three Fahrenheit temperatures 41,32 and 212 to a list of tuples containing Fahrenheit temperatures and their celcius equivalents.
fahrenheit = (41,32,212)
result = list(map(lambda x: (x, (x- 32) * (5/9)) , fahrenheit))
print(result)

#Two dimensional lists
a = [[77,68,86,73],[96,87,89,81],[70,90,86,81]] #this list generates 3 Rows and 4 columns
for row in a:
    for item in row:
        print(item, end= ' ') #end= ' ' Leaves spaces between variables
        print()

#Finish first chapter: Lists, tuples, Lambda, filter, map, if/ if else / elif, for / while

#Dictionaries in python
country_codes = {'Finland' : 'fi', 'South Africa' : 'za', 'Nepal': np}
print(country_codes)
print(len(country_codes))

print(country_codes['Finland'])
print(country_codes['South Africa'])
print(country_codes['Nepal'])

for item in country_codes.keys():
    print(item, end= ' ')

for item in country_codes.values():
    print(item, end= ' ')

print(list(country_codes.keys()))
print(list(country_codes.values()))
print(list(country_codes.items()))

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'IV': 5}
print(roman_numerals['I'])
roman_numerals['IV'] = 4 #dictionaries are mutable objects.
print(roman_numerals)

print(len(roman_numerals))
print(list(roman_numerals))
print(list(roman_numerals.keys()))
print(list(roman_numerals.values()))
print(list(roman_numerals.items()))
print()

#adding a new item to your dictionary
roman_numerals['V'] = 5
print(roman_numerals)
print()
#delete an item from your dictionary
del roman_numerals['III']
print(roman_numerals)

print(roman_numerals['V'])
print(roman_numerals.get('V'))

print('V' in roman_numerals)
print('III' in roman_numerals)

#EXP:
months = {'January': 1, 'February': 2, 'March': 3}
print(len(months))
print(list(months))
print(list(months.keys()))
print(list(months.values()))
print(list(months.items()))
print()