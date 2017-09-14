import sys
all_data = sys.stdin.read().split('\n')
a=int(all_data[0])
for x in range(a):print("*"*a+"x"*a+"*"*a)
for x in range(a):print(" "*a+"x"*a+"x"*a)
for x in range(a):print("*"*a+" "*a+"*"*a)