print("Use loops concepts")

#1.Print numbers from 1 to 20
print("Print numbers from 1 to 20")
for i in range(1,21):
    print(i)

#2. print all even number from 2 to 50
print("print even numbers from 2 to 50")
for i in range(2,51,2):
    print("Even numbers is:",i)

#3. print all odd number from 1 to 50
print("Print odd numbers from 1 to 50")
for i in range(1,51,2):
    print("odd number",i)

#4. print the square of numbers from 1 to 15
print("Print the square of numbers from 1 to 15")
for i in range(1,16):
    print(f"square {i} = {i*i}")

#5. print the cube of the number from 1 to 10  
print("print the cube of number from 1 to 10") 
for i in range(1,11):
    print(f"cube of {i} = {i*i*i}")

#6. print numbers from 10 to 1 in reverse order
print("Print reverse the number from 10 to 1")
for i in range(10,0,-1):
    print("Reverse number:",i)

#7. print a multipilaction tables of 5
print("Print a tables of 5")
for i in range(1,11):
    print(f"5*{i}={5*i}")

#8. print all character of string one by one
print("Print the string")
name="monisha"
for i in name:
    print(i)

#9. print numbers divisible by 3 between 1 and 30
print("Print the number divisible by 3 between 1 and 30")
for i in range(1,31):
    if i%3==0:
        print(f"{i}")