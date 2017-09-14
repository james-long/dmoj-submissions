i=int(input())
marks=0
for x in range(i):
     marks+=int(input())
s=int(input())
for x in range(1,s+1):
     marks+=int(input())
     print("%.3f"%(marks/(i+x)))