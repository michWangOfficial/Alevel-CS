def convert(string):
    li = list(string.split(" "))
    return li
 
def bubbleSort(thelist):
    length = len(thelist)
    for index in range(0,len(thelist)):
        for position in range(0,length-1):
            if thelist[position] > thelist [position+1]:
                temp = thelist[position]
                thelist[position] = thelist[position+1]
                thelist[position+1] = temp

print ("Enter the list with space between items")
list1 = input()
list1 = convert(list1)
print (list1)

for index in range(0, len(list1)):
    list1[index] = int(list1[index])

print (list1)

bubbleSort(list1)
print(list1)
