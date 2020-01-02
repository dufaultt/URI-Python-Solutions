#Tristan Dufault 2020-01-02
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/2518

import math

while True:
    try:
        numsteps = int(input())

        inp = input()
        inpl = inp.split(" ")

        h = float(inpl[0])
        c = float(inpl[1])
        l = float(inpl[2])

        h2 = h*numsteps
        c2 = c*numsteps

        m1 = l
        m2 = (h2*h2) + (c2*c2)
        m2 = float(math.sqrt(m2))

        r = m1*m2
        ans = r/10000
        print('{:0.4f}'.format(ans))
    except EOFError:
        break
#end whilte
