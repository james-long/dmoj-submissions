import sys
all_data=sys.stdin.read().split('\n')
lst,total=[0],0
for x in range(1,int(all_data[0])+1):lst.append(int(all_data[x]))
lst.append(0)
for x in range(1,len(lst)-1):
     if lst[x-1]<=41 and lst[x]<=41 and lst[x+1]<=41:total+=1
print(total)