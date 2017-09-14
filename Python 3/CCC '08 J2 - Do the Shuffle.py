import sys
all_data = sys.stdin.read().split('\n')
lst=["A","B","C","D","E"]
for x in range(0,len(all_data)-1,2):
     if all_data[x]=="1":
          for x in range(int(all_data[x+1])):
               lst.insert(5,lst[0])
               lst.remove(lst[0])
     elif all_data[x]=="2":
          for x in range(int(all_data[x+1])):
               transition=lst[4]
               lst.remove(lst[4])
               lst.insert(0,transition)
     elif all_data[x]=="3":
          for x in range(int(all_data[x+1])):
               lst[0],lst[1]=lst[1],lst[0]
     else:
          for x in range(5):
               print(lst[x],end=" ")