# Linear Search in an Unordered List

# declare a list of values to operate on
items = [6, 9, 19, 20, 23, 41, 49, 54, 56, 89]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    
    return None


print(find_item(41, items))
print(find_item(25, items))
