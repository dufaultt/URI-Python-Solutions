#Tristan Dufault 2019-07-03
import math

while True:
    try:
        inp = input()
        inpl = inp.split(" ")

        x = int(inpl[0])
        y = int(inpl[1])

        xf = math.factorial(x)
        yf = math.factorial(y)

        ans = xf+yf

        print(ans)

    except EOFError:
        break
