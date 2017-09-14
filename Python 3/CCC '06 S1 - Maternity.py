import sys;all_data=sys.stdin.read().split("\n");num=set()
bob,alcs,poss=all_data[0],all_data[1],[]
def possibility(let):
     lst=[]
     x=bob[(ord(let)-65)*2:(ord(let)-65)*2+2]
     y=alcs[(ord(let)-65)*2:(ord(let)-65)*2+2]
     if let.lower() in x and let.lower() in y:lst.append(let.lower())
     if let in x or let in y:lst.append(let)
     return lst
for x in "ABCDE":poss.append(possibility(x))
for x in range(3,int(all_data[2])+3):
     AC=True
     for y in range(5):
          if all_data[x][y] not in poss[y]:print("Not their baby!");AC=False;break
     if AC:print("Possible baby.")
          