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
