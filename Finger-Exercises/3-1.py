# Finger Exercise 3.1
# Write a program that asks the user to enter an interger and prints two integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should print a message to that effect.

x = int(input('enter an integer: '))

root2 = 0
while root2**2 < abs(x):
    root2 = root2 + 1
if root2**2 == x:
    print("pwr: 2", "root:", root2)

root3 = 0
while abs(root3**3) < abs(x):
    root3 = root3 + 1
if abs(root3**3) == abs(x) and x < 0:
    print("pwr: 3", "root:", -root3)
elif abs(root3**3) == abs(x) and x > 0:
    print("pwr: 3", "root:", root3)
    
root4 = 0
while root4**4 < abs(x):
    root4 = root4 + 1
if root4**4 == x:
    print("pwr: 4", "root:", root4)
    
root5 = 0
while abs(root5**5) < abs(x):
    root5 = root5 + 1
if abs(root5**5) == abs(x) and x < 0:
    print("pwr: 5", "root:", -root5)
elif abs(root5**5) == abs(x) and x > 0:
    print("pwr: 5", "root:", root5)
    
if root2**2 != x and root3**3 != abs(x) and root4**4 != x and root5**5 != abs(x):
    print("Sorry, integer entered is not a perfect power between 2 and 5")
