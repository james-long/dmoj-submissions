import sys
all_data=sys.stdin.read().split('\n')
rad,rads,total=int(all_data[0]),int(all_data[0])**2,0
for x in range(1,rad+1):
     for y in range(1,rad+1):
          if x**2+y**2<=rads:total+=1
print(total*4+rad*4+1)