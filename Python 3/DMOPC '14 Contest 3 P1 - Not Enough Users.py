import sys
all_data = sys.stdin.read().split('\n')
first=int(all_data[0])
second=int(all_data[1])
for x in range (int(all_data[2])):
     first*=second
print(first)