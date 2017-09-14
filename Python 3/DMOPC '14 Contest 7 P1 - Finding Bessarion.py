import sys;all_data = sys.stdin.read().split('\n')
loc=all_data.index("Bessarion")
if (all_data[loc-1]=="Leslie" and all_data[loc+1]=="Bayview") or (all_data[loc+1]=="Leslie" and all_data[loc-1]=="Bayview"):print("Y")
else:print("N")