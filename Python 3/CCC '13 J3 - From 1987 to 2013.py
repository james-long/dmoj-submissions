import sys
all_data=sys.stdin.read().split('\n')
a=int(all_data[0])
b=True
while b:
     a+=1
     used=[]
     for x in str(a):
          if x not in used:
               used.append(x)
          else:
               break
     if len(used)==len(str(a)):
          print(a)
          b=False