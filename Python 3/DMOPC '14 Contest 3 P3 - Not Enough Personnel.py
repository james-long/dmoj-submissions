employees=[]
empskill=[]
newskill=[]
newadapt=[]
def findteacher(minskill,maxskill):
     potential=[]
     for x in empskill:
          if minskill<=x<=maxskill:
               potential.append(x)
     if potential==[]:
          return False
     else:
          potential.sort()
          return potential[0]
for x in range(int(input())):
     a=input().split(" ")
     employees.append(a[0])
     empskill.append(int(a[1]))
for x in range(int(input())):
     b=input().split(" ")
     minskill=int(b[0])
     maxskill=int(b[0])+int(b[1])
     teach=findteacher(minskill,maxskill)
     if teach==False:
          print("No suitable teacher!")
     else:
          print(employees[empskill.index(teach)])