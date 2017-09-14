import sys;all_data=sys.stdin.read().split("\n")
lst,num=[],0
for x in range(1,len(all_data)-1):
     isrt=False
     for y,z in enumerate(lst):
          if int(all_data[x])>z:lst.insert(y,int(all_data[x]));isrt=True;break
     if isrt==False:lst.append(int(all_data[x]))
     num+=lst.index(int(all_data[x]))+1
print("%.2f"%(round(num/int(all_data[0]),2)))