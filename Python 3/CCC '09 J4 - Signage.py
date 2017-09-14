import sys;all_data=sys.stdin.read().split('\n')
num,words,sign=int(all_data[0]),["WELCOME","TO","CCC","GOOD","LUCK","TODAY"],[]
while len(words)>0:
     temp=[]
     for x in words:
          if sum(len(y) for y in temp)+len(x)<=num:temp.append(x);temp.append(".");words=words[1:]
          else:break
     temp=temp[:-1]
     sign.append(temp)
for x in sign:
     if "." not in x:x.append("."*(num-sum(len(y) for y in x)))
     else:
          dot=1
          while sum(len(y) for y in x)<num:
               if "."*dot in x:x[x.index("."*dot)]="."*(dot+1)
               else:dot+=1
for x in sign:
     for y in x:print(y,end="")
     print()