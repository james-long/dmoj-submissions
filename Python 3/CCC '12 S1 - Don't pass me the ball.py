import sys
all_data = sys.stdin.read().split('\n')
if int(all_data[0])<4:print(0)
else:
    a,b,c,total=int(all_data[0])-3,int(all_data[0])-2,int(all_data[0])-1,0
    for x in range(1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if x<y<z<int(all_data[0]):total+=1
    print(total)