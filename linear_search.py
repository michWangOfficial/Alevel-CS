list1 = ["1","2","3","4","5","6","7","8","9","10"]
left = 0
found = 0

def list1Search(itemName):
    global left
    global found
    while found == 0 or left >= len(list1):
        if list1[left] == itemName:
            found = 1
            
        else:
            if left <= 9:
                left += 1
            else: 
                continue

        

print ("What you wanna seach?")
itemSearch = input("")
list1Search(itemSearch)
if found == 0:
    print("Not found with the length", len(list1)) 
else:
    print("Item found with index", left+1)
