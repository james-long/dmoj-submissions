import sys
all_data=sys.stdin.read().split("\n")
ctr,msg,times=int(all_data[-2])*[0],[],[]
for x in range(1,int(all_data[0])+1):
     msg.append(len(all_data[x]))
for x in range(len(msg)):
     besttime=2001
     for y in range(len(ctr)):
          if ctr[y]<besttime:besttime=ctr[y]
     times.append(ctr.index(besttime)+1)
     ctr[ctr.index(besttime)]+=msg[x]
for x in range(len(times)):print(times[x])