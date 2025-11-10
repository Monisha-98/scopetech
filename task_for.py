#1. Print all the number between 1 to 100 that are divisible by 6 not divide by 9
for n in range (1,101):
    if n%6==0 and n%9!=0:
        print(n)

#2. find the sum of odd number between 1 to 50
print("The odd number between 1 to 50")
sum=0
for n in range(1,51):
    if n%2!=0:
        sum=sum+n
print(sum)    


#3. count how many numbers between 1 and 200 are divisible by both 4 and 6.
print("Count the number between 1 and 200 divisible by both 4 and 6")
c=0
for a in range(1,201):
    if a%12==0:
        c=c+1
print("Total numbers are:",c)

#4. print the mulitiplication table of the given number n from 1 to 10
print("Multiplication for a given number")
m=int(input("Enter the number:"))
for i in range(1,11):
    res=m*i
    print(f"{m}*{i}={res}")

#5. find the factorial of the given number n
print("Find the factorial number")
n=int(input("Enter the number for factorial:"))
fact=1
for i in range(1,n+1):
    if n>0:
        fact=fact*i
    print("The factorial is:",fact)

#6. print all prime numbers form between 1 to 50 using a single loop and flag 
print("Print the prime number between 1 to 50")
for n in range(2,51):
    flag=1
    for i in range(2,n):
        if n % i==0:
            flag=0
            break
        if flag==1:
            print(n)

#7. calculate the sum of digits of a number using a arithmetic
print("Sum of digits of a given number using arithmetic")
n=int(input("Enter the number for sum:"))
sum=0
for i in range(1,n):
    num=n%10
    sum=sum+num
    n=n//10
print(sum)

#8. count how many numbers between 1 to 500 are perfect cube
print("Count the perfect cube between 1 to 500")
co=0
for c in range(1,201):
    cube=c**3
    if cube <=200:
        print(cube)
        co=co+1
    else:
        break
print("Total cubes are:",co)

#9. print the reverse of the number using arithmetic only
print("Print the reverse number")
n=int(input("Enter the number for reverse:"))
rev=0
while n!=0:
    num=n%10
    rev =rev*10+num
    n=n//10
print(rev)

#10 print numbers from 1 to 100 but skip numbers ending with digit 5
print("skip the number that end with digit 5")
for n in range(1,101):
    if n%10==5:
        continue
    print(n)