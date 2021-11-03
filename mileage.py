print("How many kms did you run today ?")
km = input() # input result is str by default
# print(type(km))
miles = round(float(km)/1.60934, 2)
print(f"ok input pris pour {km} -> {miles} miles")
