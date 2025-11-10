#1. write a program to print Right triangle
print("Print right triangle")
for i in range(1, 6):
    for j in range(5, i, -1):   
        print(" ", end="")
    for k in range(1, i + 1):   
        print(k, end="")
    print()

#2. write a program to print left triangle
print("print the left triangle")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#3. write a program to print square
print("print square")
for i in range(1, 5):
    for j in range(1,5):   
        print(j, end=" ")
    print()

#4. write a program to print 8
print("Print the number 8")
for i in range(1,6):
    for j in range(1,5):
        if i==1 or i==3 or i==5:
            print("*",end=" ")
        elif j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#5. write a program to print the hollow square
print("Print the hollow square")
n=int(input("Enter the number for square:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#6. write a program to print the hollow right triangle
print("print the hollow right triangle")
n=int(input("Enter the number for triangle:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#7. write a program to print inverse left triangle
n = int(input("Enter the size of the triangle: "))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

#8. write a program to print inverse right triangle
n = int(input("Enter the size of the triangle: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
