if True:
    print("the condition is true")

# Basic Grammar
language = "Python"
language = "Javascript"
language = "Java"
if language == "Python":
    print("The language is Python")
elif language == "Javascript":
    print("The Language is Javascript")
else:
    print("None of it is a language")

# object is
list1 = [1,3,3]
list2 = [1,3,3]
list3 = list1
print(list1 == list2) #True
print(list1 is list2) #False, coz their ids are not the same
print(id(list1), id(list2))
print(list1 is list3) #True, their ids are same

# False cases
condition = False
condition = 0
condition = ""
condition = []
condition = ()
condition = {}
if not condition:
    print("the condition is false")

# and or not
user = "Admin-b"
log_in = True
if user == "Admin" and log_in: 
    print("Welcome")
elif not log_in:
    print("Hello, pls log in")
else: 
    print("NO Cred")