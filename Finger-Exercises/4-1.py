# Finger Exercise 4.1
# Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the build-in str operation in.

x = input('Enter first string: ')
y = input('Enter second string: ')

def isIn(a,b):
    if a in b or b in a:
        return True
    else:
        return False

print(isIn(x,y))
