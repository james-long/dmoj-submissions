import sys,math;all_data=sys.stdin.read().split("\n")[1:-1]
lst=[]
for x in all_data:lst.append(int(x.split()[1])-int(x.split()[0]))
print(max(lst))