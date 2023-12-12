import math
import random
import time

y = 0
x = 0

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

list1 = []
for index in range(0,10000):
    list1.append(random.randint(0,999999))

for index in range(0, len(list1)):
    list1[index] = int(list1[index])

x = time.time()

bubbleSort(list1)
print(list1)

y = time.time()

print(y-x)
