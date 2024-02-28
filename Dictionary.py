Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

#2. Nested dict
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)

# 3. Adding items
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

#4. Get function
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accessing a element using get:")
print(Dict.get(3))

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using key:")
print(Dict[1])

#5. Accessing elements of Nested
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

#6. Delete items
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =")
print(Dict)
del (Dict[1])
print("Data after deletion Dictionary=")
print(Dict)

#7. functions on dict
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())

#7. Merge two dict.
def Merge(dict1, dict2):
    return (dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)

#function to merge two dict
def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1


# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

