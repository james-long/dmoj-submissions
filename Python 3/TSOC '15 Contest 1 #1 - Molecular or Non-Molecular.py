import sys;all_data=sys.stdin.read().split("\n")[1:]
ltr=['Cl','Br','Xe','Kr','Si','As','Rn','Ne','He','H','C','N','O','F','P','S','I']
for x in all_data:
     yn=False
     for y in x.split():
          if y not in ltr:print("Not molecular!");yn=True;break
     if not yn:print("Molecular!")