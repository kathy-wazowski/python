'''
1. once import the module, the codes in the module will be executed
2. my_module.func_name()
3. import my_module as mm
4. from my_module import find_index as fi, test
5. from my_module import *    #this can't track down which function is from my_module
6. import sys  print(sys.path)
7. import module from a different directory.  
   a. import sys   sys.path.append("path to your module") 
   b. change the python environment variable
   11:48 how to change the python environment variable. after changing it, you can import the module from CMD. still in the text-editor, you can't directly import it. 
8. random.choice(list)
9. datetime.date.today()  calendar.isleap(2019)
10. os.getcwd()  cwd: current working directory  os._file_
11. import antigravity
'''
import sys
# !!! sys.path must contain directories, not files
sys.path.append("D:/")
from sec_module import find_index, testTxt #though the text editor showed error, still it works.
# from my_module import *
courses = ["Math", "Art", "Physics"]
search_txt = "Art"
print(testTxt)
print(find_index(search_txt, courses))
import random
print(random.choice(courses))
import datetime
import calendar
print(datetime.date.today())
print(calendar.isleap(2024))
import os
print(os.getcwd())
print(os.__file__)
import antigravity
