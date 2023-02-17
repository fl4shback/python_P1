print("How many kms did you run today ?")
km = input() #request user input
miles = round(float(km)/1.60934, 2) #input returns a string, need to convert it to float and round it before operations and display
print(f"Conversion de {km} km en miles -> {miles} miles")
