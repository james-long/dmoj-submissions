import sys
all_data=sys.stdin.read().split('\n')
parts,miss="BFTLC",False
for x in parts:
     if all_data[0].find(x)==-1:
          print(x)
          miss=True
if miss==False:print("NO MISSING PARTS")