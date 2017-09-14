import sys
all_data=sys.stdin.read().split('\n')
ariv=int(all_data[0][:2])*3600+int(all_data[0][3:5])*60+int(all_data[0][6:])
strt=int(all_data[1][:2])*3600+int(all_data[1][3:5])*60+int(all_data[1][6:])
print(strt-ariv)