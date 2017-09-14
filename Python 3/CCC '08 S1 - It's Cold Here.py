import sys;all_data=sys.stdin.read().split("\n");cold,city,all_data=201,"@",all_data[:len(all_data)-1]
for x in all_data:
     y,z=x.split()
     if int(z)<cold:cold=int(z);city=y
print(city)
     