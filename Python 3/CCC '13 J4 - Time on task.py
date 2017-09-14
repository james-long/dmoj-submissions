import sys
all_data=sys.stdin.read().split('\n')
lst=[]
total=int(all_data[0])
current=0
num=0
for x in range(2,int(all_data[1])+2):
     lst.append(all_data[x])
lst.sort()
while current<=total:
     if len(lst)==0:
          break
     elif current+int(lst[0])>total:
          break
     else:
          current+=int(lst[0])
          num+=1
     lst=lst[1:]
print(num)