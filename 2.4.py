# Finger Exercise 2.3
# Replace the comment in the following code with a while loop
# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# #concatenate X to toPrint numXs times
# print(toPrint)

n = int(input('How many times should I print the letter X? '))
reps = n
toPrint = ''

if reps < 0:
    print("Sorry, invalid value")
else:
    while reps > 0:
        toPrint = toPrint + 'X'
        reps = reps - 1
print(toPrint)
