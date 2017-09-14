import sys;cur,fin,wgt,blank=sys.stdin.read().split("\n")
cur,fin,wgt=int(cur),int(fin)-.5,int(wgt)
cur*=((100-wgt)/100)
cur=round(cur,2)
if cur+wgt<fin:print("DROP THE COURSE")
else:
     need=fin-cur
     final=need/wgt*100
     if final%1>=0.5:final=int(final+1)
     else:final=int(final)
     if final<0:final=0
     print(final)