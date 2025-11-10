#9. write a program to print the patterns as shown below
print("Pattern 1")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("Pattern 2")
n = int(input("Enter the size of the triangle: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Pattern 3")
n=int(input("Enter the number for triangle:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

print("Pattern 4")
n = int(input("Enter number of rows: "))
ch = 65 
for i in range(1, n + 1):
    print(chr(ch) * i)
    ch += 1

print("Pattern 5")
ch=65
n=5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
    print()
    

print("Pattern 6")
n = int(input("Enter number of rows: "))
ch = 65 
for i in range(1, n + 1):
    print(chr(ch) * i)
    ch += 1

print("Pattern 7")
n=5
for i in range(1, n + 1):
    ch = 65  
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
    print()