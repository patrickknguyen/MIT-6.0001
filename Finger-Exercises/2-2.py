# Finger Exercise 2.2
# Write a program that examines three variables--x, y, and z--and prints the largest odd number among them. If none of them are odd, it should print a message to that effect

x = int(input("Input a number for x: "))
y = int(input("Input a number for y: "))
z = int(input("Input a number for z: "))

if x % 2 == 0:
    x = 0
if y % 2 == 0:
    y = 0
if z % 2 == 0:
    z = 0
 
if x == y and x == z and x > 0:
    print("x, y, and z,", str(x) + ", are the same odd number")

elif x == y and x > z:
    print("x and y,", str(x) + ", are the largest odd numbers")
elif x == z and x > y:
    print("x and z,", str(x) + ", are the largest odd numbers")
elif y == z and y > x:
    print("y and z,", str(y) + ", are the largest odd numbers")   
 
elif x > y and y > z:
    print("x,", str(x) + ", is the largest odd number")
elif y > z:
    print("y,", str(y) + ", is the largest odd number")
elif z != 0:
    print("z,", str(z) + ", is the largest odd number")

if x + y + z == 0:
    print("there are no odd numbers")
