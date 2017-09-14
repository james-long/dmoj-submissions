import sys
all_data = sys.stdin.read().split('\n')
if int(all_data[0])<6:
     print(int(all_data[0])//2+1)
else:
     print(int(all_data[0])//2+1-(int(all_data[0])-5))