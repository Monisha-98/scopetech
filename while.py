#1. print number from 10 down 1
print("print number from 10 down to 1")
i=10
while i>=1:
    print(i)
    i=i-1

#2.Find the sum of even digits in the number
#48293=4+8+2=14
print("Sum of even digits in the number")
n=[4,8,2,9,3]
i=0
sum=0
while i<len(n):
    if n[i]%2==0:
        print("The number is even number",n[i])
        sum=sum+n[i]
    i=i+1
print("The sum of number is",sum)    
    
#3. Find the number of digits in the given number
h=int(input("Enter the numbers"))
h=abs(h)
if h==0:
    count=1
else:
   count=0
while h>0:
        h=h//10
        count=count+1
        print("number of digits",count)

#4. check the number is palindrome
print("Check the number is palindrome")
nas=int(input("Enter the numbers"))
pal=nas
rev=0
while nas>0:
        digit=nas%10
        rev=rev*10+digit
        nas=nas//10
if pal==rev:        
        print("its palindrome")
else:
     print("its not pallindrome")

#5.find the reverse the number
a=int(input("Enter the numbers"))
a=abs(a)
h1=a
rev=0
while a>0:
        num=a%10
        rev=rev*10+num
        a=a//10
        
print("reversed number",rev)   

#6. Print the fibbonici series upto 100
print("Print the fibonici series")
a=0
b=1
while a<=100:
    print(a,end="")
    sum=a+b
    a=b
    b=sum

#7. compute the power of a number manually without ** or pow()
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
count = 0
while count < exponent:
    result = result * base   
    count = count + 1        
print("Result:", result)

#8. Keep dividing a number by 2 untill it becomes lessthan one and count how many division
n = float(input("Enter a number: "))
count = 0
while n >= 1:
    n = n / 2
    count = count + 1
print("Number of divisions:", count)

#9. print the digits of a number from last to first one per line
print("print the digits from last to first")
v = int(input("Enter a number: "))
while v > 0:
    la = v % 10          
    print(la)            
    v = v // 10

#10. compute the sum of square of digits of a number 
#example 123=1^2+2^2+3^2=14
u = int(input("Enter a number: "))
u=abs(u)
sum=0
while u > 0:
    sq = u % 10          
    sum=sum+sq**2            
    u = u // 10
print("The sum of square:",sum)






