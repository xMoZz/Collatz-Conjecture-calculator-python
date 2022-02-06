import math
import time 


def Repeat():
    z =int(input("If you want to try a new number write 1: "))
    if z == 1:
        Main()

    else:
        print("Shutting down")
        time.sleep(1)
      

def Main():
    print("!Collatz Conjecture!")
    x = int(input("Enter a number: "))

    while x != 1:    
        if (x % 2) == 0:
            x = x/2
            print(x)
        else:
            x = x*3+1
            print(x)

    input("Now it is a loop")

    Repeat()

Main()