import sys;all_data=sys.stdin.read().split("\n")
if all_data[0].count(" ")==1:maxx,maxy=all_data[0].split(" ")
else:maxx,maxy=all_data[0][:-1].split(" ")
maxx,maxy,x,y=int(maxx),int(maxy),0,0
for z in range(1,len(all_data)-2):
     if all_data[z].count(" ")==1:xmove,ymove=all_data[z].split(" ")
     else:xmove,ymove=all_data[z][:-1].split(" ")
     x+=int(xmove)
     y+=int(ymove)
     if x>maxx:x=maxx
     elif x<0:x=0
     if y>maxy:y=maxy
     elif y<0:y=0
     print(x,y)