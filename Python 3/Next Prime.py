import sys
all_data=sys.stdin.read().split("\n")
number=int(all_data[0])
def isprime(num):
     for x in range(2,int(num**0.5)+1):
          if num%x==0:
               return False
     return True
if number==1:
     print("2")
else:
     if isprime(number):
          print(number)
     else:
          while True:
               number+=1
               if isprime(number):
                    print(number)
                    break