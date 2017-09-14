import sys
all_data = sys.stdin.read().split('\n')
a,b,c=int(all_data[0]),int(all_data[1]),int(all_data[2])
if a+b+c==180:
     if a==b==c:print("Equilateral")
     elif a==b or b==c or a==c:print("Isosceles")
     else:print("Scalene")
else:print("Error")