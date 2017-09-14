import sys
all_data = sys.stdin.read().split('\n')
lst=[]
for x in range(len(all_data)-1):lst.append(int(all_data[x]))
if lst[0]<lst[1]<lst[2]<lst[3]:print("Fish Rising")
elif lst[0]>lst[1]>lst[2]>lst[3]:print("Fish Diving")
elif lst[0]==lst[1]==lst[2]==lst[3]:print("Fish At Constant Depth")
else:print("No Fish")