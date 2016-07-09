print("Hello, World!")

# lines that start with '#' are comments and not executed

print("---------------------------------")
print()
print()

# this is how you make new variables and give them values
x = 13
my_other_variable = "My favorite number is"

# use print() to display messages
print(my_other_variable, x)

print("---------------------------------")
print()
print()

x = x * 2 # you would never see x=2x in math, but it's fine here! the right side is evaluated first

# functions encapsulate some routine
def print_favorite_number(z):
    # 'my_other_variable' is the same as before
    # but 'x' has been overwritten by the 'local scope'!
    print(my_other_variable, z)

# so far we've only defined our function, but haven't used it yet
print_favorite_number(x)
print_favorite_number(2 * 2 + 7)

print("---------------------------------")
print()
print()

# if, for, and while control where your program goes
if x > 100:
    print("that's a big favorite number")
elif x < 0:
    print("your favorite number is less than zero??")
else:
    print("Good choice.")

# an 'array' is a sequence of variables
myArray = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

for i in range(10):
    # brackets 'index' into the array
    print(i, myArray[i])

i = 0
while i < 10:
    print(i, myArray[i])
    i = i + 1

print("---------------------------------")
print()
print()

# a 'dictionary' is like an array with names
myDictionary = {'favorite_number': x, 'caffeinated': True}
print(myDictionary)

# I can add to or remove from my dictionary
myDictionary['twelve'] = 12
del(myDictionary['favorite_number'])
print(myDictionary)

# I can loop over my dictionary too
for key,value in myDictionary.items():
    print("the key is", key, "and the value is", value)

print("---------------------------------")
print()
print()