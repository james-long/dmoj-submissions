import sys
all_data = sys.stdin.read().split('\n')
nik,byr,a,b,c,d,s=0,0,int(all_data[0]),int(all_data[1]),int(all_data[2]),int(all_data[3]),int(all_data[4])
if s>=(a+b):
     nik+=s//(a+b)*(a-b)
     nikrem=s%(a+b)
     if nikrem!=0:
          if nikrem>a:nik+=a-(nikrem-a)
          elif nikrem<a:nik+=nikrem
else:
     if s>a:nik+=a-(s%a)
     else:nik+=a
if s>=(c+d):
     byr+=s//(c+d)*(c-d)
     byrrem=s%(c+d)
     if byrrem!=0:
          if byrrem>c:byr+=c-(byrrem-c)
          elif byrrem<c:byr+=byrrem
else:
     if s>c:byr+=c-(s%c)
     else:byr+=c
if nik>byr:print("Nikky")
elif byr>nik:print("Byron")
elif byr==nik:print("Tied")