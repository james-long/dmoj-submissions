import sys,re;all_data=sys.stdin.read().split('\n')
if all_data[0]=="1":print(all_data[1].split()[0])
elif all_data[0]!="1" and all_data[0]!="0":
     lst=[]
     for x in all_data[1:-1]:
          name,r,s,d=x.split()
          lst.append([int(r)*2+int(s)*3+int(d),name])
     lst.sort()
     a=[x[0] for x in lst]
     if a.count(lst[-1][0])>1:
          num=lst[-1][0]
          namelst=[x[1] for x in lst if x[0]==num]
          namelst.sort()
          print(namelst[0]+"\n"+namelst[1])
     elif a.count(lst[-2][0])>1:
          num=lst[-2][0]
          namelst=[x[1] for x in lst if x[0]==num]
          namelst.sort()
          print(lst[-1][1]+"\n"+namelst[0])
     else:
          print(lst[-1][1]+"\n"+lst[-2][1])