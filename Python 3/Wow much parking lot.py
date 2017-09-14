import sys
all_data=sys.stdin.read().split('\n')
x,y=0,0
for z in range(1,int(all_data[0])*2,2):
     if all_data[z]=="North":y+=int(all_data[z+1])
     elif all_data[z]=="South":y-=int(all_data[z+1])
     elif all_data[z]=="East":x+=int(all_data[z+1])
     else:x-=int(all_data[z+1])
print(x,y)