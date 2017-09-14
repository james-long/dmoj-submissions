a,b,i=0,0,"@"
while i!="7":
     i=input()
     if i[0]=="1":
          if i[2]=="A":a=int(i[4:])
          else:b=int(i[4:])
     elif i[0]=="2":
          if i[2]=="A":print(a)
          else:print(b)
     elif i[0]=="3":
          if i[2]=="A":
               if i[4]=="A":a=a*2
               else:a+=b
          if i[2]=="B":
               if i[4]=="A":b+=a
               else:b=b*2
     elif i[0]=="4":
          if i[2]=="A":
               if i[4]=="A":a=a**2
               else:a=a*b
          if i[2]=="B":
               if i[4]=="A":b=b*a
               else:b=b**2
     elif i[0]=="5":
          if i[2]=="A":
               if i[4]=="A":a=0
               else:a=a-b
          if i[2]=="B":
               if i[4]=="A":b=b-a
               else:b=0
     elif i[0]=="6":
          if i[2]=="A":
               if i[4]=="A":a=1
               else:a=int(a/b)
          if i[2]=="B":
               if i[4]=="A":b=int(b/a)
               else:b=1