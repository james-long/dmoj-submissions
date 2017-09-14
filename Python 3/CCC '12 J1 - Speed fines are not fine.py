import sys
all_data = sys.stdin.read().split('\n')
a,b=int(all_data[0]),int(all_data[1])
if a>=b:print("Congratulations, you are within the speed limit!")
else:
     if b-a<21:fine=100
     elif b-a<31:fine=270
     else:fine=500
     print("You are speeding and your fine is $%i."%fine)