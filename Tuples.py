# 1.Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# 2. Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# 3. Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

# 4. Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# 5. Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

#6. Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# 7.creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

#8. Remove empty tuples form the list
def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))

#Mirroe image N=3 paradox  paizwlc
# function to mirror characters of a string

def mirrorChars(input, k):
    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))

    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k - 1]
    suffix = input[k - 1:]
    mirror = ''

    # change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]

    # concat prefix and mirrored part
    print(prefix + mirror)


# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input, k)


# Two separate lists using zip() function
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
               "Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
    print ( "Car: %s, Accessory required: %s"  % (c, a))


# Function to change string to a new character

def newString(charSet, input):
    # map original character set of english
    # onto new character set given
    origCharSet = 'abcdefghijklmnopqrstuvwxyz'
    mapChars = dict(zip(charSet, origCharSet))

    # iterate through original string and get
    #  characters of original character set
    changeChars = [mapChars[chr] for chr in input]

    # join characters without space to get new string
    print(''.join(changeChars))


# Driver program
if __name__ == "__main__":
    charSet = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    newString(charSet, input)