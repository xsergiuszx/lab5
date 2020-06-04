#import sys
#x = 0
#while(x<1000):
#    x = x+5
#    print(x)
#else:
#    print("Przekroczyles limit") 

liczby=[3, 4, 2, 1, 6, 5, 10, 11, 18, 25, 35, 89, 90, 110, 111] 
 
for x in liczby:
    if (x%5==0):
        print(str(x)+" ")
else:
    print("Dotarles do konca") 
