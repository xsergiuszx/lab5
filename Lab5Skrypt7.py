import sys
x = 1
while(x>0):
    print("Podaj liczbe, ktorej kwadrat chcesz uzyskac")
    print("Wpisz 0 by wyjsc")
    s=sys.stdin.readline()
    x = int(s)
    print(pow(x,2))
else:
   print("Koniec")
