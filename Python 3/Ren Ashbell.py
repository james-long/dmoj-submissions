import sys
all_data=sys.stdin.read().split('\n')
yn=True
for x in range(2,int(all_data[0])+1):
     if int(all_data[x])>=int(all_data[1]):
          print("NO")
          yn=False
          break
if yn:print("YES")