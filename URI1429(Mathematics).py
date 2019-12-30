#Tristan Dufault 2019-12-30
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1429
import math

inp = input()

while(inp != 0):
    inpl = [int(d) for d in str(inp)]
    size = len(inpl)
    ans = 0
    for i in range(size):
        ans = ans + (inpl[i]*math.factorial(size-i))

    print(ans)
    #end for
    inp = int(input())
#end while
