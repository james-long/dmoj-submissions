import sys;ori,new,dec,blank=sys.stdin.read().split("\n")
code1,code2=[],[]
for x in range(len(ori)):
     if len(code1)<27:
          if ori[x] not in code1:code1.append(ori[x]);code2.append(new[x])
     else:break
for x in dec:
     if x in code2:print(code1[code2.index(x)],end="")
     else:print(".",end="")