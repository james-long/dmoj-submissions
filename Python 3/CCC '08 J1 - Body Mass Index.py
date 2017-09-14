import sys
all_data = sys.stdin.read().split('\n')
if float(all_data[0])/(float(all_data[1])**2)>25:
     print("Overweight")
elif float(all_data[0])/(float(all_data[1])**2)<18.5:
     print("Underweight")
else:
     print("Normal weight")