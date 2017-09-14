import sys
all_data = sys.stdin.read().split('\n')
cases=[100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
total=1691600
for x in range(1,int(all_data[0])+1):
     total-=int(cases[int(all_data[x])-1])
if total/(10-int(all_data[0])) < int(all_data[len(all_data)-2]):
     print("deal")
else:
     print("no deal")