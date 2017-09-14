input()
logs=input()
cnt=0
lst=[]
for i in logs:
     if i=="O": cnt+=1
     else:
          if cnt>0:
               lst.append("O"*cnt)
               cnt=0
if cnt>0:
     lst.append("O"*cnt)
if not lst: print("0")
else:
     print(len(lst))
     for i in lst:
          print(i)