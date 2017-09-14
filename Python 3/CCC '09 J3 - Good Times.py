import sys;all_data=sys.stdin.read().split('\n')
orig=int(all_data[0])
print("%i in Ottawa"%orig)
names=["Victoria","Edmonton","Winnipeg","Toronto","Halifax","St. John's"]
for x,y in enumerate(names):
     if y!="St. John's":
          time=orig-300+x*100
          if time>2359:time-=2400
          elif time<0:time+=2400
          print("%i in %s"%(time,y))
     else:
          time=orig-370+x*100
          if time>2359:time-=2400
          elif time<0:time+=2400
          if int(str(time)[-2:])>60:
               time=int(str(time)[:-2])*100+100+int(str(time)[-2:])-60
          print("%i in %s"%(time,y))