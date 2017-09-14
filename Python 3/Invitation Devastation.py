import sys
all_data=sys.stdin.read().split("\n")
count=all_data[0].count(">")
for x in range(2,int(all_data[1])+2):
     for y in range(count):
          text=all_data[0].replace(">",all_data[x])
     if count==0:print(all_data[0])
     else:print(text)