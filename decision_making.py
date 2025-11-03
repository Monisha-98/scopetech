print("Decision Making concepts")

#1 Write a Python program to check whether a number is positive, negative, or zero.
print("positive,negative,or zero")
a=int(input("Enter a number :"))
if(a>0):
 print("positive")   
elif(a<0):
  print("negative")
else:
 print("The number is zero")
 
 #2 Write a program to check whether a number is even or odd
 print("The given number is odd or even")
e=int(input("Enter a number:"))
if e%2==0:
 print(e,"is even")        
else:
 print(e,"is odd")

 #3 Write a program to check if a person is eligible to vote (age ≥ 18).
print("check your eligible to vote are not")
age=int(input("Enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

 #4 Write a program to check if a student passed or failed based on marks.
print("To check the student get passed are failed")   
marks=int(input("Enter your marks:"))
if  marks>=40:
          print("you are passed")
else:
      print("you are failed")

 #5 Write a program to find the largest of two numbers.
print("To find the largest number")     
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
  print("The largest number is:",num1)
elif num2<num1:
      print("The lagest number is:",num2)
else:
    print("Both numbers are equal")

#6 Write a program to display grade (A, B, C, D, Fail) based on marks.
print("To display the marks based on grade")
stu_mark=int(input("Enter a total mark:"))
if stu_mark>90 and stu_mark<=100:
    print("A Grade")
elif stu_mark>70 and stu_mark<=90:
    print("B Grade")
elif stu_mark>50 and stu_mark<=70:
     print("C Grade")
elif stu_mark>30 and stu_mark<=50:
    print("D Grade")
else:
    print("fail")

#7 Write a program to print the day name based on a number (1–7)
print("To print the day name based on the number")    
day=int(input("Enter a number 1-7:"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("No more days")

#8 Write a program to check whether a character is an alphabet, digit, or special character
print("To check the given character are alphabet,digit and special character")    
a=input("Enter any character")
if len(a) !=1:
  if a.isalpha():
    print("is an alphabet")
  elif a.isdigit():
    print("is an digit")
else:
    print("It is an special character")

#9 Write a program to find the largest among three numbers
print("Largest among three numbers")    
n1=int(input("Enter a first number:"))
n2=int(input("Enter a second number:"))
n3=int(input("Enter a third number:"))
if n1>n2 and n1>n3:
 print("First number is greater")
elif n2>n1 and num2>n3:
  print("second number is greater")
else:  
  print("The third number is greater")

#10  Write a program to display a message based on temperature (e.g., Hot, Warm, Cool, Cold)
print("Display message based on temperature")  
temp=float(input("Enter the temperature"))
if temp>=100:
  print("Hot")
elif temp>80 & temp<=100:
  print("Warm")
elif temp> 30 & temp <=80:
  print("Cool")
else:
    print("Cold")

#11 Write a program to check whether a number is positive and even using nested if    
print("Positive and even using nested if")
pos = int(input("Enter a number: "))
if pos>0:
    if pos%2==0:
        print("The Number is positive and even")
    else:
        print("The number is postive and odd number")
else:
    print("The number is not positive")

#12 Write a program to simulate a login system that checks username and password using nested if    
print("Login system")    
username = input("Enter your name: ")
password = input("Enter your password: ")
x = "Moni"
y = "12345678"
if x == username:
    if y == password:
        print("Login was successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

#13 Write a program to check if a person is eligible for a job:
#	Must be above 18
#	Must have experience
print("To check he is eligible for a job")
age = int(input("Enter your age: "))
exp = input("Do you have experience (type yes/no): ")
if age>18:
    if exp == "yes":
        print("You are eligible for the job")
    else:
        print("You don't have experience")
else:
    print("You must be above 18")

#14  Write a program to check if a year is leap year or not using if-else
print("To check it is leap year or not")    
year=int(input("Enter a leap year:"))
if (year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#15  Write a program to check whether a student qualifies for a scholarship:
#	Marks ≥ 85
#	Attendance ≥ 90%
print("To check the student qualifies for scholarship")
m = int(input("Enter your marks: "))
attend = float(input("Enter your attendance percentage: "))
if m>80:
    if attend>=95:
        print("You Qualify for the scholarship!")
    else:
        print("You need at least 95% attendance")
else:
    print("You need at least 80 marks") 


    