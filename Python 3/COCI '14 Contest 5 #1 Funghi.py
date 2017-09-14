import sys
all_data = sys.stdin.read().split('\n')
lst,best=[],0
for x in range(8):lst.append(int(all_data[x]))
for x in range(4):lst.append(int(all_data[x]))
a=lst[0]+lst[1]+lst[2]+lst[3]
for x in range(1,8):
     if lst[x]+lst[x+1]+lst[x+2]+lst[x+3]>a:a=lst[x]+lst[x+1]+lst[x+2]+lst[x+3]
print(a)