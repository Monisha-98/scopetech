#1.	Create 5 variables of different data types (int, float, str, bool, list).
#Use print() and type() to display each variable and its type.

print("Using basic concept")
print("To display the five variables and its type")
a=int(input("Enter the number"))
b=float(input("Enter the float number"))
c=input("Enter the name")
d=True
e=['a',2,3.4,True]
print("The datatype is:",type(a))
print("The datatype is:",type(b))
print("The datatype is:",type(c))
print("The datatype is:",type(d))
print("The datatype is:",type(e))

#2.	Print a sentence using variables:
#Example output — “My name is John and my age is 15.”
#(But the name and age must come from variables.)
print("To print the name and age")
name=input("Enter the name:")
age=int(input("Enter the age:"))
print(f"My name is {name} and my age is {age}")

#3. Take two numbers as variables and print their sum, difference, product, and quotient.
print("Do the arithmetic operations")
sum1=int(input("Enter the first number"))
sum2=int(input("Enter the second number"))
print("The addition:",sum1+sum2)
print("The subtraction:",sum1-sum2)
print("The product:",sum1*sum2)
print("The quotient :",sum1/sum2)

#4. Print the result of combining string and integer properly using f-string (avoid type error)
print("Combining the string and integer")
str=input("Enter the name:")
eum=int(input("Enter the number:"))
print(f"The string is {str} The integer is{eum}")

#6.	Use arithmetic operators to find:
#	Square of a number
#	Cube of another number
#	Average of three numbers
print("Using arithmetic operator we find square,cube and average number")
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
print("The square of the number:",n1*2)
print("The cube of a number :",n2*3)
print("The average of three number is:",n1+n2+n3/3)

#7. Compare two variables a and b using all relational operators (>, <, ==, !=, >=, <=).
#Print True or False for each case.
print("Using relational operater")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The number is greater:",a>b)
print("The number is Lesser:",a<b)
print("The number is equal:",a==b)
print("The number is greater than are equal to:",a>=b)
print("The number is lesser than are equal to:",a<=b)

#8. Use logical operators (and, or, not) to check:
#	If a number is positive and even
#	If a number is negative or zero
print("Using logical operator")
g=int(input("Enter the first number:"))
g2=int(input("Enter the second number:"))
print("The given number is positive and even",g>0 & g%2==0)
print("The given number is negative or zero",g<0 | g==0)

#9.  Write a program to swap two variables without using a third variable (use arithmetic or assignment operators)
print("Swap two variables without third variable")
print("Using arithmetic operator")
p=int(input("Enter the number:"))
p1=int(input("Enter the number:"))
p=p+p1
p1=p-p1
p=p-p1
print("After Swapping")
print("First number:",a)
print("Second number:",b)
print("Using assignment operator")
a,b=b,a
print("First number:",a)
print("Second number:",b)

#10 Take two numbers and check:
#	Which one is greater
#	Whether both are equal
#(Use conditional and comparison operators)
print("Check the number is greater and equal")
k=int(input("Enter the First number"))
k1=int(input("Enter the second number"))
if k>k1:
    print("The first number is greater")
else:
    print("The second number is greater")
print("The number is equal",k==k1)

#11 Write a program that checks whether a given number is even or odd
print("The given number is odd or even")
e=int(input("Enter a number:"))
if e%2==0:
 print(e,"is even")        
else:
 print(e,"is odd")

#12 Write a program to find whether a number is positive, negative, or zero (use elif)
print("Check whether the number is positive,negative or zero")
o=int(input("Enter the number1:"))
if o>0:
   print("The number is positive")
elif o<0:
   print("The given number is negative")
else:
   print("The given number is zero")

#13 Take a student’s mark and print:
#	“Grade A” if mark ≥ 90
#	“Grade B” if mark between 75 and 89
#	“Grade C” if mark between 50 and 74
#	“Fail” if below 50
m=int(input("Enter the mark for 100:"))
if m>=90:
   print("A Grade")
elif m>=75 and m<=89:
   print("B Grade")
elif m>=50 and m<=74:
   print("C Grade")
else:
   print("Fail")

#14. Check if a year is a leap year or not.
#(Hint: divisible by 4, but not 100, unless divisible by 400)
print("Find the year is leap are not")
year=int(input("Enter the year"))
if (year % 400 == 0) or (year % 4== 0 and year % 100 != 0):
      print("This is leap year:")
else:
   print("This is not a leap year")

#15 Write a program to check whether a person is eligible to vote (age ≥ 18).
#If not eligible, print how many years left to become eligible.
print("To check the eligibility to vote")
vote=int(input("Enter the age:"))
if vote>=18:
   print("Eligible to vote")
elif vote<18:
   print("You have still",18-vote,"years to vote")
else:
   print("Invalid")

#16 Write a program that takes three numbers and prints which one is the largest
print("TO print which number is largest")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter the third number:"))
if num1>=num2  and num1>=num3:
  print("The largest number is:",num1)
elif num2>=num1 and num2>=num3:
      print("The lagest number is:",num2)
else:
    print("The largest number is:",num3)

#17 Using nested if, check:
#	If a number is positive
#	Check if it’s even or odd
#	Else print it’s negative or zero
print("Check it is postive,even or odd and negative or zero")
h=int(input("Enter the number:"))
if h>0:
   print("The number is positive")
   if h%2==0:
      print("The number is even")
   else:
      print("The number is odd")
else:
    print("The number is negative or Zero")

#18 Using nested if, print:
#	“Child” if age < 13
#	“Teen” if age between 13–19
#	“Adult” if age between 20–59
#	“Senior Citizen” if age ≥ 60
print("Print its child,teen,adult or senior citizen")
age=int(input("Enter the age"))
if age>=0:
     if age< 13:
         print("It's Child")
     elif age>=13 and age<=19:
        print("It's Teen")
     elif age>=20 and age<=59:
        print("It's Adult")
     elif age>=60:
        print("It's Senior citizen")
     else:
        print("Invalid")
   
#19 Write a program that checks whether a character is a vowel or consonant.
#(Input a single alphabet letter and use if-elif-else.)
print("Check the vowels")
w=input("Enter the vowels")
vow=['a','e','i','o','u','A','E','I','O','U']
if w in vow:
   print("It's vowels")
elif w.isalpha():
   print("It's consonant")
else:
   print("Invalid")

#20 Take three subject marks from a student.
#	If all marks ≥ 40 → print “Pass”
#	If any one subject < 40 → print “Fail”
#	If average ≥ 90 → print “Outstanding” (use nested if)
print("Print the mark of the student")
m1 = int(input("Enter your English Mark: "))
m2 = int(input("Enter your Tamil Mark: "))
m3 = int(input("Enter your Maths Mark: "))
total = m1+m2+m3
if m1>=40 and m2>=40 and m3>=40:
    print("Pass")
    avg = total/3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")
    






