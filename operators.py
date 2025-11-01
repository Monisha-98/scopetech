print("Operators")
#1Addtion of two number
a=int(input("Enter the a number:"))
b=int(input("Enter the b number:"))
c=a+b
print("Add of two number:",c)

#2Subtraction of two number
value1=int(input("Enter First Number:"))
value2=int(input("Enter second Number:"))
sub=value1-value2
print("Subtraction:",sub)


#3Multiplication of two number
sum1=int(input("Enter sum1 Number:"))
sum2=int(input("Enter sum2 Number:"))
mul=sum1*sum2
print("Multiplication:",mul)

#4Division of two number
div1=int(input("Enter div1 Number:"))
div2=int(input("Enter div2 Number:"))
divi=div1/div2
print("Division:",divi)


#5find remainder of two number
rem1=int(input("Enter rem1 Number:"))
rem2=int(input("Enter rem2 Number:"))
rem=rem1%rem2
print("Remainder:",rem)


#6 Square of a number
s=int(input("Enter a Number:"))
s1=s**2
print("Square of a number is:",s1)


#7 cube of a number
c1=int(input("Enter a Number:"))
c2=c1*3
print("Cube of a given number is:",c2)

#8 Average of three number
a1=int(input("Enter a first Number:"))
a2=int(input("Enter a second Number:"))
a3=int(input("Enter a third Number:"))
avg=a1+a2+a3/3
print("Average of a number is:",avg)

# Swap two variables
s1=int(input("Enter the first swapping number:"))
s2=int(input("Enter the second swapping number:"))
s=s1
s1=s2
s2=s
print("After swapping the number:",)
print("First number:",s1)
print("Second number:",s2)

#10 Check Datatype
val=int(input("Enter the value for datatype:"))
print("The value is:",val)
print("The given values datatype is:",type(val))

#11 Add Integer and Float
mat=int(input("Enter the integer value:"))
mat1=float(input("Enter the float value:"))
mat2=mat+mat1
print("The value is:",mat2)
print("After the added value:",type(mat2))

#12 Simple Comparison
com=int(input("Enter the first comparision:"))
com1=int(input("Enter the Second comparision:"))
print("The given comparision is:",com>com1)

#13Check Equal or Not
n1=int(input("The first number to find equal is:"))
n2=int(input("The second number to find equal is:"))
print("Check equal given number is equal are not:",n1==n2)

#14Find total and average marks
mark1=int(input("The mark1:"))
mark2=int(input("The mark2:"))
mark3=int(input("The mark3:"))
mark4=int(input("The mark4:"))
mark5=int(input("The mark5:"))
total=mark1+mark2+mark3+mark4+mark5
print("The total mark is:",total)
avg=mark1+mark2+mark3+mark3+mark4+mark5/5
print("The average is:",avg)

#15Convert hours to mintutes
hours=int(input("Enter the hours:"))
minutes=hours*60
print("Hours convert to minutes:",minutes)

#16Calculate the simple interest
p=int(input("Enter the principal:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))
si=(p*r*t)/100
print("The simple interest:",si)

#17 Find area of rectangle
l=int(input("The length is "))
b=int(input("The breath is:"))
rec=l*b
print("The area of rectangle is:",rec)

#18 Check postivie or not
pos=int(input("Enter the postive:"))
print("Postive:",pos>0,"Negative:",pos<0,"Zero:",pos==0)

#19 Calculate the total cost
name=input("Enter the name of product:")
cost=int(input("Enter the cost of item:"))
quantity=int(input("Enter the quantity:"))
tc=cost*quantity
print("The single product cost is:",cost)
print("The Total cost of item is:",tc)

#20 Small Calculator
cal=int(input("Enter the number1:"))
cal1=int(input("Enter the number2:"))
add=cal+cal1
subt=cal-cal1
muli=cal*cal1
div=cal/cal1
print("Addition:",add)
print("Addition:",subt)
print("Addition:",muli)
print("Addition:",div)



