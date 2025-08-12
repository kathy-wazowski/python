print("Entering my_module")
def find_index(to_search, target):
    for index, item in enumerate(target): 
        if to_search == item:
            return index
    return -1
testTxt = "Test Text"
