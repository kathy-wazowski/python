'''
1. key word def to define a function and keyword pass, it returns None 
2.chain the function, say_hello().upper() 
3. error shows if not passing in the argument required unless a default value is provided.
   when pass in the argument with a default value, need to assign the argument, 
   for example: name = "Jack", this is called keyword arguments. 
   Actually directly passing in "Jack" is also OK.
4. *args, **kwargs  kwargs means keyword arguments, for example student_info("Math", "Art", name="Jack", age=12), *args is a tuple and **kwargs is a dictionary. Not that there're double * before kwargs.
5. pass in list and dictionary.  add * and ** before them as arguments. for example:  student_info(*course_list, **info_map)
6. doc string helps to define what the function does. 
7. Python can combine the comparing operators.  1 <= month <= 12
'''
# pass
def first_func():
    pass

# chain func
def say_hello():
    return "Hi, there"
print(say_hello().upper())

# error shown if argument required
def say_hello(greeting):
    print(f"{greeting}, there")
# say_hello() # this will cause an error

# default argument
def say_hello(greeting, name="stranger"):
    print(f"{greeting}, {name}.")
say_hello("Hi")
say_hello("Hello", "Kathy") # directly pass in "Kathy" is ok, name="Kathy" is also ok

# *args, **kwargs
def student_info(*args, **kwargs):
    print(args,kwargs)
student_info("Math", "Art", name="Kathy", age=37) # *args is a tuple, **kwargs is a dictionary

# pass in list and dictionary
courses = ["Math", "Art"]
info={"name": "Kathy", "age":37}
student_info(*courses, **info);

# doc string
def ibm_healthy(weight, height):
    '''Based on the weight and height, to determine if the IBM is healthy'''
    pass

# combine comparing operators
def valid_month(month):
    if not 1 <= month <= 12:
        return "invalid"
    else:
        return "ok"
print(valid_month(13))
print(valid_month(3))