import sys
all_data = sys.stdin.read().split('\n')
marks=[]
for x in range(1,int(all_data[0])+1):
     marks.append(int(all_data[x]))
marks.sort()
if len(marks)%2==0:
     a=(marks[int(all_data[0])//2-1]+marks[int(all_data[0])//2])/2
     if a%1>=0.5:
          print(int(a)+1)
     else:
          print(int(a))
else:
     print(marks[int(all_data[0])//2])