import sys
all_data = sys.stdin.read().split('\n')
answers=[]
num=int(all_data[0])
for x in range(1,num+1):
     answers.append(all_data[x])
numWA=answers.count("WA")
numWAintoAC=int(numWA*0.3)
numIRintoAC=10
numIRintoWA=10
for x in answers:
     if x=="AC":
          print(x)
     elif x=="WA":
          if numWAintoAC>0:
               print("AC")
               numWAintoAC-=1
          else:
               print("WA")
     elif x=="TLE":
          print("WA")
     else:
          if numIRintoAC>0:
               print("AC")
               numIRintoAC-=1
          elif numIRintoWA>0:
               print("WA")
               numIRintoWA-=1
          else:
               print("IR")
          