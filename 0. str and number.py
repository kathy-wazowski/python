Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
3+2
5
print("Hello world :D")
Hello world :D
rent=1220
gas = 202.5
groceries=305.6
print(rent)
1220
total = rent + gas + groceries
print(total)
1728.1
rent = 1400
item1="rent"
item2 = "gas"
item3 = "groceries"
print("Expenses Items: ", item1, item2, item3)
Expenses Items:  rent gas groceries
True=4
SyntaxError: cannot assign to True
foo + bar = 4
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
12+34
46
3-4
-1
3/4
0.75
4*5
20
11%2
1
3**2
9
2**4
16
clear
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
clear()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
import os
os.system('cls')
0
msg = "Hello World"
msg[:5]
'Hello'
msg[6:]
'World'
greeting = "Hi"
name="Kathy"
msg = f"{greeting}, {name.toupper()}. Welcome!"
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    msg = f"{greeting}, {name.toupper()}. Welcome!"
AttributeError: 'str' object has no attribute 'toupper'. Did you mean: 'isupper'?
msg=f"{greeting}, {name.isupper()}. Gorgeous"
msg
'Hi, False. Gorgeous'
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
msg=f"{greeting}, {name.upper()}. Sweaty"
msg
'Hi, KATHY. Sweaty'
num = 5
num1 = 3.3
type(num)
<class 'int'>
type(num1)
<class 'float'>
num = -2
abs(num)
2
3/2
1.5
5//2
2
num = 8
num *= 3
num
24
num = 7,33
num = 7.89
round(num, 1)
7.9
len(num)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    len(num)
TypeError: object of type 'float' has no len()
num=9.445
round(num, 2)
9.45
num_1 = 3
num_2 = 7
num_1<num_2
True
>>> num_1 == num_2
False
>>> num_1 != num_2
True
>>> num1 = "400"
>>> num2 = "899"
>>> num1+num2
'400899'
>>> int(num1)+int(num2)
1299
>>> num = 8.9
>>> floor(num)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    floor(num)
NameError: name 'floor' is not defined. Did you mean: 'float'?
>>> import math
>>> math.floor(9.78, 1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    math.floor(9.78, 1)
TypeError: math.floor() takes exactly one argument (2 given)
>>> math.floor(9.78)
9
>>> math.ceil(7.33)
8
>>> num = "8.33"
>>> float(num)
8.33
