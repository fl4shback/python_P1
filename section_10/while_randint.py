from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 1  # i should be incremented by one each iteration

while number != 5:
    number = randint(1, 10)
    i += 1
print(f"GG you got {number} after {i} iterations")
