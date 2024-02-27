# 1.Initializing List
List1 =[1, 'A', 2, 'B', 'C']
print(List1)

#2. Initializing Empty List
List2=[]
print(List2)
#or
List3=list()
print(List3)
print(type(List1))  #type of list

#3. Order matters
a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
b = [ 1, 2, 5, "Ram", 3.50, "Rahul", 6 ]
print(a == b)

#4. List Indexing and Splitting
list = ["A", "B", "C", "D", "E", "F"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
# Slicing the elements
print(list[0:6])
# By default, the index value is 0 so its starts from the 0th element and go for index -1.
print(list[:])
print(list[2:5])
print(list[1:6:2])

list = [1,2,3,4,5]
print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-3:-1])

# 5.updating list values
list = [1, 2, 3, 4, 5, 6]
print(list)
# It will assign value to the value to the second index
list[2] = 10
print(list)
# Adding multiple-element
list[1:3] = [89, 78]
print(list)
# It will add value at the end of the list
list[-1] = 25
print(list)

# 6. repetition of list
list1 = [12, 14, 16, 18, 20]
l = list1 * 2
print(l)

# 7.concatenation of two lists
list1 = [12, 14, 16, 18, 20]
list2 = [9, 10, 32, 54, 86]
l = list1 + list2
print(l)

# 8.size of the list
list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
print(len(list1))

# 9.iteration of the list
list1 = [12, 14, 16, 39, 40]
for i in list1:
    print(i)

# 10. membership of the list
list1 = [100, 200, 300, 400, 500]
# true will be printed if value exists
# and false if not
print(600 in list1)
print(700 in list1)
print(1040 in list1)

# 11. Append will add the item in the last index
# Declaring the empty list
l =[]
#Number of elements will be entered by the user
n = int(input("Enter the number of elements in the list:"))
# for loop to take the input
for i in range(0,n):
    # The input is taken from the user and added to the list as the item
    l.append(input("Enter the item:"))
print("printing the list items..")
# traversal loop to print the list items
for i in l:
    print(i, end = "  ")

# 12. Remove items from list
list = [0,1,2,3,4]
print("printing original list: ");
for i in list:
    print(i,end=" ")
list.remove(2)
list.pop(3)
print("\nprinting the list after the removal of first element...")
for i in list:
    print(i,end=" ")

# 13. Max, Min and Length Function
list1 = [103, 675, 321, 782, 200]
print(max(list1))
print(min(list1))
print(len(list1))

# 14. Create a program to eliminate the List's duplicate items.
list1 = [1,2,2,3,55,98,65,65,13,29]
# Declare an empty list that will store unique values
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# 15.  Accessing elements from a multi-dimensional list
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks'], ['Name', 'Place']]
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
print(List[2][0])

# 16. Append to add items
List = []
print("Initial blank List: ")
print(List)
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# 17. Adding elements Insert()
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)

#18. Extend()
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)

#20. Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

#21. Reversed function List
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)

#22. Remove()
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

#23. Multiple element remove
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)

#24 . Pop()
List = [1, 2, 3, 4, 5]
List.pop()
print("\nList after popping an element: ")
print(List)
List.pop(2)
print("\nList after popping a specific element: ")
print(List)

#25. # Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

# Driver code
newList = [12, 35, 9, 56, 24]

#25. # Python3 program to Merge first and last
# elements separately in a list of lists

lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
a = []
for i in lst:
    a.extend(i)
x = []
y = []
for i in range(0, len(a)):
    if(i % 2 == 0):
        x.append(a[i])
    else:
        y.append(a[i])
res = []
res.append(x)
res.append(y)
print(res)

print(swapList(newList))