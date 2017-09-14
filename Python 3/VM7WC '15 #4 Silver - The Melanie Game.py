import sys
all_data=sys.stdin.read().split('\n')
p,k=3,int(all_data[0])
for x in all_data[1]:
     x=ord(x)-p-k
     while x<65:x+=26
     print(chr(x),end="")
     p+=3