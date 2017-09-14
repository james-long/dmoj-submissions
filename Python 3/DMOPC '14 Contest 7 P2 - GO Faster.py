import sys;all_data=sys.stdin.read().split('\n')
worig=int(all_data[1].split()[0])
borig=worig
wothers,bothers=0,0
for stop in all_data[2:-1]:
     on,off=stop.split()
     if worig>0:
          if worig>=int(off):worig-=int(off)
          else:wothers-=(int(off)-worig);worig=0
     else:wothers-=int(off)
     if bothers>0:
          if bothers>=int(off):bothers-=int(off)
          else:borig-=(int(off)-bothers);bothers=0
     else:borig-=int(off)
     wothers+=int(on)
     bothers+=int(on)
print(worig)
print(borig)