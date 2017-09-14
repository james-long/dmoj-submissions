import sys
all_data = sys.stdin.read().split('\n')
a,e=int(all_data[0]),int(all_data[1])
if a>2 and e<5:print("TroyMartian")
if a<7 and e>1:print("VladSaturnian")
if a<3 and e<4:print("GraemeMercurian")