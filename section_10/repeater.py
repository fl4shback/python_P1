reps = int(input("How many reps ?"))
i = 0
while i < reps:
    i += 1
    print(f"Yelling {i} time{'s'[:i^1]} !!!")

#### CORRECTION
# times = input("How many times do I have to tell you? ")
# times = int(times)

# # Simplest Version
# for time in range(times):
# 	print("CLEAN UP YOUR ROOM")

# # Version 2
# for time in range(times):
# 	print(f"time {time+1}:CLEAN UP YOUR ROOM")
