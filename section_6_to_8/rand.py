from random import randint
num = randint(1, 1000) #picks random number from 1-1000
print(num)
if num % 2 != 0:
    print("not even")
else:
    print("even")
