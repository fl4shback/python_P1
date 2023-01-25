from random import randint
num = randint(1, 1000) #picks random number from 1-1000
print(num)
if num % 2 != 0:
    print("even")
else:
    print("not even")