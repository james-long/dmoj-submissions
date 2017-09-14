import sys
all_data = sys.stdin.read().split('\n')
ant,dav=100,100
for x in range(1,int(all_data[0])+1):
     if int(all_data[x][:1])>int(all_data[x][2:]):dav-=int(all_data[x][:1])
     elif int(all_data[x][:1])<int(all_data[x][2:]):ant-=int(all_data[x][2:])
print(ant)
print(dav)