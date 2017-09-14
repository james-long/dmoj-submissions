import sys
all_data = sys.stdin.read().split('\n')
row=["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ -.@"]
col=["AGMSY","BHNTZ","CIOU ","DJPV-","EKQW.","FLRX@"]
pos="A"
x1,y1=0,0
x2,y2=0,0
dist=0
all_data[0]+="@"
for x in all_data[0]:
     for a in range(5):
          if x in row[a]:
               x2=row[a].find(x)
               break
     for a in range(6):
          if x in col[a]:
               y2=col[a].find(x)
               break
     dist+=(abs(x1-x2)+abs(y1-y2))
     x1,y1=x2,y2
print(dist)