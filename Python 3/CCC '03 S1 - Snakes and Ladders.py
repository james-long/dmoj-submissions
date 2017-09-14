current,sp1,sp2=1,[54,90,99,9,40,67],[19,48,77,34,64,86]
while True:
     a=input()
     if a=="0":
          print("You Quit!")
          break
     else:
          if current+int(a)<101:current+=int(a)
          if current in sp1:current=sp2[sp1.index(current)]
          print("You are now on square %i"%current)
          if current==100:
               print("You Win!")
               break