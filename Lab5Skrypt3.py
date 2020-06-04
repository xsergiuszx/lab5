import sys
import math
print("Podaj pierwsza liczbe")
a=sys.stdin.readline()
print("Podaj druga liczbe")
b=sys.stdin.readline()
print("Podaj trzecia liczbe")
c=sys.stdin.readline()
a = int (a)
b = int (b)
c = int (c)
if 0 < a < 10:
    print ("a miesci sie w przedziale 0-10")
else:
    print ("a nie miesci sie w przedziale 0-10")
if a>b:
     print("a jest wieksze od b")
else:
     print("a nie jest wieksze od b")
if b>c:
      print("b jest wieksze od c")
else:
      print("b nie jest wieksze od c")
