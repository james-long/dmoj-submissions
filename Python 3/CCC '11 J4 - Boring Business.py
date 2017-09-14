import sys;all_data=sys.stdin.read().split("\n")[:-2]
done,curr=[(-1,-5),(-1,-6),(-1,-7),(0,-1),(0,-2),(0,-3),(0,-7),(1,-3),(1,-7),(2,-3),(2,-7),(3,-3),(3,-4),(3,-5),(3,-7),(4,-5),(4,-7),(5,-3),(5,-4),(5,-5),(5,-7),(6,-3),(6,-7),(7,-3),(7,-4),(7,-5),(7,-6),(7,-7)],(-1,-5)
for x in all_data:
     direc,num=x.split()
     hit,num="safe",int(num)
     if direc=="d":
          for y in range(num):
               curr=(curr[0],curr[1]-1)
               if curr in done:hit="DANGER";
               else:done.append(curr)
     elif direc=="u":
          for y in range(num):
               curr=(curr[0],curr[1]+1)
               if curr in done:hit="DANGER"
               else:done.append(curr)
     elif direc=="l":
          for y in range(num):
               curr=(curr[0]-1,curr[1])
               if curr in done:hit="DANGER"
               else:done.append(curr)
     else:
          for y in range(num):
               curr=(curr[0]+1,curr[1])
               if curr in done:hit="DANGER"
               else:done.append(curr)
     print("%i %i %s"%(curr[0],curr[1],hit))
     if hit=="DANGER":break