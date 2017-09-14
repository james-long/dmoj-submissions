import sys;lst=sys.stdin.read().split("\n")[:-2][::-1]
for x in range(0,len(lst)-1,2):
     lr="LEFT"
     if lst[x]=="L":lr="RIGHT"
     print("Turn %s onto %s street."%(lr,lst[x+1]))
lr="LEFT"
if lst[-1]=="L":lr="RIGHT"
print("Turn %s into your HOME."%lr)