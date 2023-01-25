#### MY SOLUTION
for nb in range(1, 21):
    if nb % 2 == 0 and not nb == 4:
        state = "even"
    elif nb % 2 != 0 and not nb == 13:
        state = "odd"
    else:
        state = "unlucky"
    print(f"{nb} is {state}")

#### COURSE SOLUTION
# Main Solution
# for num in range(1,21):
# 	if num == 4 or num == 13:
# 		print(f"{num} is unlucky")
# 	elif num % 2 == 0:
# 		print(f"{num} is even")
# 	else:
# 		print(f"{num} is odd")

	
# # Slight Refactor
# for num in range(1,21):
# 	if num == 4 or num == 13:
# 		state = "unlucky"
# 	elif num % 2 == 0:
# 		state = "even"
# 	else:
# 		state = "odd"
# 	print(f"{num} is {state}")
