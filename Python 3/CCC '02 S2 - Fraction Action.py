import sys
all_data=sys.stdin.read().split('\n')
a=int(all_data[0])
b=int(all_data[1])

if a==0:
     print("0")
elif a==b:
     print("1")

if a>b:
     for x in range(b,0,-1):
          if a%x==0 and b%x==0:
               a//=x
               b//=x
     if a//b>0:
          print(a//b,end=" ")
     if a%b>0:
          print(str(a%b)+"/"+str(b))
elif a<b:
     for x in range(a,0,-1):
          if a%x==0 and b%x==0:
               a//=x
               b//=x
     if a//b>0:
          print(a//b,end=" ")
     if a%b>0:
          print(str(a%b)+"/"+str(b))