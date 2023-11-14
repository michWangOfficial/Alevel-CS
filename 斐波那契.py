attempts = 0
x1 = int(input())
x2 = int(input())
x3 = int(0)
while True:
  x3 = x1
  x1 = x2
  x2 = x1 + x3
  print (x2)
  x3 = 0
  attempts = attempts + 1 
  if x2 > 500000:
    break