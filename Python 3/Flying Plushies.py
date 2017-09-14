import sys
all_data=sys.stdin.read().split('\n')
h,times=int(all_data[0]),0
for x in range(2,int(all_data[1])+2):
     if int(all_data[x])>=h:times+=1
print(times)