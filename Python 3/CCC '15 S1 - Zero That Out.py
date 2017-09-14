import sys;all_data=sys.stdin.read().split("\n")[1:-1]
lst=[]
for x in all_data:
     if x=="0":lst.pop()
     else:lst.append(int(x))
print(sum(lst))