print("List functions")
#1. reverse the given number l=[100,200,300,400,500]
print("Reverse the given number of list")
l=[100,200,300,400,500]
ele=l[::-1]
print("Reversed list:",ele)

#2. concatenate two list l1=["hello","madam"],l2=["Dear","sir"]
print("concatenate two list")
l1=["hello","madam"]
l2=["dear","sir"]
a=l1+l2
print("After concatenate:",a)

#3. remove the empty string of a given list l1=["pen","","pencil","eraser","","scale"]
print("Remove the empty strings")
li1=["pen","","pencil","eraser","","scale"]
li1.remove("")
li1.remove("")
print("After removed the list is:",li1)

#4. write a python program to convert the string to the list
print("Convert string to list")
name="Monisha Sankar"
print("After convertion :",list(name))

#5. check if the list contains the element list=[1,2,3,'a','b','c']
print("Check the elements present in the list")
m=[1,2,3,'a','b','c']
e1='a'
e2='b'
e3='c'
c=(e1,e2,e3)
for e in c:
    if e in m:
        print(f"{e} element is present in list")
    else:
        print(f"{e} element is not in the list")

#6. Remove all elements from a list
print("Remove all elements")
m1 = [1, 2, 3, 'a', 'b', 'c']
m1.clear()
print(m1)

#7. Count the occurrence of a specific object in a list
#pets = ["dog","cat","fish","fish","cat"]
print("count the occurrence of a specific object")
pet = ['dog', 'cat', 'fish', 'fish', 'cat']
cc = pet.count('cat')
print(f"'cat' appears {cc} times in the list")


#8. Return the length of a list
print("Return the length of our list")
pets = ['dog', 'cat', 'fish', 'fish', 'cat']
length = len(pets)
print("The length of the list is:", length)

#9. Insert a value at a specific index in an existing list
print("Insert a value at a specific index in an existing list")
fruits = ['apple', 'banana', 'cherry']
print("before list" ,fruits)
fruits.insert(1, 'orange')
print("After insert:" ,fruits)

#10. Write a Python program to clone or copy a list.
print("Write a Python program to clone or copy a list")
original = [1, 2, 3, 4, 5]
cloned = original.copy()
print("Original List:", original)
print("Cloned List:", cloned)

#11. Write a Python program to extend a list without append.
print(" Extend a list without append.")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print("Extended List:", l1)

#12. Remove duplicates from a list  
#li = [3, 2, 2, 1, 1, 1]
print("Remove duplicate from a list")
li = [3, 2, 2, 1, 1, 1]
print("Before removing:",li)
unique = list(set(li))
print("List after removing duplicates:", unique)

#13. Find the index of the 1st matching element
print("Index of the 1st matching element")
num = [3, 5, 7, 5, 9, 5]
value = num.index(5)
print("The first occurrence of 5 is at index:", value)

#14. check if an element is not in a list
print("check if an element is not in a list")
num1 = [1, 2, 3, 4, 5]
print("The list is :",num1)
num2 = int(input("Enter a number to check: "))
if num2 not in num1:
    print(f"{num2} is not in the list")
else:
    print(f"{num2} is in the list")

#15. Write a Python program to create a list of 5 numbers and print it.
print("Create a list and print it")
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("The list of numbers is:", numbers)

#16. Write a program to find the length of a list using len().
print("length of a list")
n = [10, 20, 30, 40, 50]
length = len(n)
print("The length of the list is:", length)

#17. Write a program to access elements from a list using positive and negative indexes.
print("access the element from the list")
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
print("Using positive indexes:")
print("fruits[0] =", fruits[0])
print("fruits[2] =", fruits[2])
print("fruits[4] =", fruits[4])
print("\nUsing negative indexes:")
print("fruits[-1] =", fruits[-1])
print("fruits[-3] =", fruits[-3])
print("fruits[-5] =", fruits[-5])

#18. Write a program to update the 3rd element of a list.
print("Update the 3rd element of a list.")
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers[2] = 99
print("Updated list:", numbers)

#19. Write a program to delete an element from a list using del.
print("Delete a list")
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
del numbers[2]
print("List after deleting 3rd element:", numbers)


#20. Write a program to append a new element to the list using append().
print("To append a element")
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)
fruits.append('mango')
print("List after appending a new element:", fruits)


#21 Write a program to insert an element at a specific position using insert().
print("Insert a element using position")
numbers = [10, 20, 30, 40]
print("Original list:", numbers)
numbers.insert(2, 25) 
print("List after inserting element:", numbers)

#22. Write a program to remove an element using remove().
print("Remove the element")
fruits = ['apple', 'banana', 'cherry', 'mango']
print("before removing",fruits)
item = input("Enter the fruit name to remove: ")
if item in fruits:
    fruits.remove(item)
    print("Updated list:", fruits)
else:
    print(f"{item} not found in the list")

#23. Write a program to remove the last element using pop().
print("Remove the last element using pop()")
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop()
print("Removed element:", removed)
print("Updated list:", numbers)

#24. Write a program to clear all elements using clear().
print("Clear all elements using clear()")
items = [input("Enter first item: "), input("Enter second item: "), input("Enter third item: ")]
print("Original list:", items)
items.clear()
print("List after using clear():", items)


#23 Write a program to print all elements of a list using a for loop.
print("Print all elements of a list using a for loop.")
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("The numbers you entered are:")
for n in numbers:
    print(n)

#24 Write a program to find the sum of all elements using sum().
print("Find the sum of all elements using sum().")
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("The sum of all elements in the list is:", total)

#25 Write a program to find the maximum and minimum values using max() and min().
print("Find the maximum and minimum values using max() and min().")
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

#26 Write a program to count how many times an element appears using count().
print("Count how many times an element appears using count().")
pets = ['dog', 'cat', 'fish', 'fish', 'cat', 'dog', 'dog']
count_dog = pets.count('dog')
print("List:", pets)
print("The word 'dog' appears", count_dog, "times.")

#27 Write a program to find the index of a specific element using index().
print("Find the index of a specific element using index().")
fruits = ['apple', 'banana', 'cherry', 'mango', 'banana']
index_value = fruits.index('cherry')
print("List:", fruits)
print("The index of 'cherry' is:", index_value)

#28 Write a program to reverse a list using reverse().
print("Reverse a list using reverse().")
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)

#29 Write a program to sort a list in ascending and descending order using sort().
print("Sort a list in ascending and descending order using sort().")
numbers = [5, 2, 9, 1, 7]
print("Original list:", numbers)
numbers.sort()
print("List in ascending order:", numbers)
numbers.sort(reverse=True)
print("List in descending order:", numbers)

#30 Write a program to copy one list to another using copy().
print("Copy one list to another using copy().")
fruits = ['apple', 'banana', 'cherry', 'mango']
print("Original list:", fruits)
new = fruits.copy()
print("Copied list:", new)

#31 Write a program to print only even numbers from a list.
print("Print only even numbers from a list.")
numbers = [10, 15, 20, 25, 30, 35, 40]
print("Before :",numbers)
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

#32 Write a program to print only odd numbers from a list.
print("Print only odd numbers from a list.")
numbers = [10, 15, 20, 25, 30, 35, 40]
print("Before:",numbers)
print("Odd numbers in the list:")
for num in numbers:
    if num % 2 != 0:
        print(num)

#33 Write a program to add two lists using + operator.
print("Add two lists using + operator.")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("First list:", list1)
print("Second list:", list2)
print("Combined list:", combined)

#34 Write a program to repeat list elements using * operator.
print("Repeat list elements using * operator.")
fruits = ['apple', 'banana', 'cherry']
r = fruits * 3
print("Original list:", fruits)
print("Repeated list:", r)

#35 Write a program to check if an element exists in a list using in.
print("Check if an element exists in a list using in.")
fruits = ['apple', 'banana', 'cherry', 'mango']
if 'banana' in fruits:
    print("Yes, 'banana' is in the list.")
else:
    print("No, 'banana' is not in the list.")

#36 Write a program to slice a list (print first 3 and last 3 elements).
print(" Slice a list ")
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
first = numbers[:3]   
last = numbers[-3:]   
print("Original list:", numbers)
print("First 3 elements:", first)
print("Last 3 elements:", last)

#37 Write a program to find the largest 2 numbers in a list.
print("Find the largest 2 numbers in a list.")
numbers = [10, 45, 32, 67, 89, 21, 90]
numbers.sort(reverse=True)
largest1 = numbers[0]
largest2 = numbers[1]
print("List:", numbers)
print("The two largest numbers are:", largest1, "and", largest2)

#38 Write a program to find duplicate elements in a list.
print("Find duplicate elements in a list.")
numbers = [1, 2, 2, 3, 4, 4, 5]
print("original list:",numbers)
duplicates = list({n for n in numbers if numbers.count(n) > 1})
print("Duplicate elements are:", duplicates)

#39 Write a program to remove duplicate elements from a list.
print("Remove duplicate elements from a list.")
numb = [3, 2, 2, 1, 1, 1]
print("Before removing:",numb)
u = []
for n in numb:
    if n not in u:
        u.append(n)
print("List after removing duplicates:", u)

#40 Write a program to merge two sorted lists into one sorted list.
print("Merge two sorted lists into one sorted list.")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("List1:",list1)
print("List1:",list2)
mer = sorted(list1 + list2)
print("Merged sorted list:", mer)

#41 Write a program to create a list of squares of numbers from 1 to 10 using a loop.
print("squares of numbers from 1 to 10 using a loop.")
squares = []   
for i in range(1, 11):
    squares.append(i * i)
print("List of squares from 1 to 10:", squares)

#42 Write a program to separate even and odd numbers into two lists.
print("Separate even and odd numbers into two lists.")
nu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ev = []
od = []
for n in nu:
    if n % 2 == 0:
        ev.append(n)
    else:
        od.append(n)
print("Even numbers:", ev)
print("Odd numbers:", od)

#43 Write a program to create a nested list (list inside a list).
print("Create a nested list (list inside a list).")
nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nest)
print("First sub-list:", nest[0])
print("Second element of First sub-list:", nest[0][2])

#44 Write a program to access elements from a nested list.
print("Access elements from a nested list.")
numbers = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print("Nested List:", numbers)
print("First sub-list:", numbers[0])
print("Second sub-list:", numbers[1])
print("Third sub-list:", numbers[2])

print("First element of first list:", numbers[0][0])
print("Second element of second list:", numbers[1][1])
print("Third element of third list:", numbers[2][2])

#45 Write a program to flatten a nested list (convert to one single list).
print("Flatten a nested list.")
neste = [[1, 2, 3], [4, 5], [6, 7, 8]]
print("Original nested",neste)
flat = []
for sublist in neste:
    for item in sublist:
        flat.append(item)
print("Flattened List:", flat)

#46 Write a program to find common elements between two lists.
print("Find common elements between two lists.")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("list item:",list1,list2)
common = []
for item in list1:
    if item in list2:
        common.append(item)
print("Common elements:", common)

#47 Write a program to find elements present in one list but not in another.
print("Find elements present in one list but not in another.")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print("Elements present in list1 but not in list2:", difference)

#48 Write a program to remove all occurrences of a specific element from a list.
print("Remove all occurrences of a specific element from a list.")
numbers = [2, 3, 4, 2, 5, 2, 6, 2]
element = 2
result = []
for num in numbers:
    if num != element:
        result.append(num)
print("Original list:", numbers)
print(f"List after removing all occurrences of {element}:", result)

#49 Write a program to convert a list into a tuple.
print("Convert a list into a tuple.")
lis = [10, 20, 30, 40, 50]
mtuple = tuple(lis)
print("Original List:", lis)
print("Converted Tuple:", mtuple)

#50 Write a program to find the average of list elements.
print("Find the average of list elements.")
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
count = len(numbers)
average = total / count
print("List:", numbers)
print("Average of list elements:", average)

#51 Write a program to count positive, negative, and zero numbers in a list.
print("Count positive, negative, and zero numbers in a list.")
n = [10, -3, 0, 5, -7, 8, 0, -2]
p = 0
ne= 0
z = 0
for num in n:
    if num > 0:
        p += 1
    elif num < 0:
        ne += 1
    else:
        z += 1
print("List:", n)
print("Count of positive numbers:", p)
print("Count of negative numbers:", ne)
print("Count of zeros:", z)

#52 Write a program to find product of all elements in a list (without using math.prod()).
print("Product of all elements in a list (without using math.prod()).")
n1 = [2, 3, 4, 5]
p = 1
for num in n1:
    p *= num
print("List:", n1)
print("Product of all elements:", p)

