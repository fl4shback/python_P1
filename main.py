print("Hello!")
string_var =  "test"
int_var = 12
float_var = 12.5
bool_var = True
dic_var = {"test" : "value", "test2" : "value2"}
list_var = ["list0", "list1"]
nested_dir_var = {0 : {"name" : "christophe", "surname" : "leduc"}, 1 : {"name" : "melanie", "surname" : "laduchesse"}}
nested_dir_var = None
print("string_var is:", type(string_var), "value:", string_var[3]) #prints only 4th character (0,1,2,3) from var
print(int_var)
print("int_var is:", type(int_var))
print(float_var)
print("float_var is:", type(float_var))
print(bool_var)
print("bool_var is:", type(bool_var))
print(dic_var)
print("dic_var is:", type(dic_var))
print(list_var)
print("list_var is:", type(list_var))
print(nested_dir_var)
print("nested_dir_var is:", type(nested_dir_var))

try:
    for key in nested_dir_var:
        print("Entrée:", key)
        print("Name: ", nested_dir_var[key]["name"])
        print("Surname: ", nested_dir_var[key]["surname"])
except:
    print("variable vide") 

if type(bool_var) == str:
    print("success")
else:
    print("failure: bool_var is not string")
