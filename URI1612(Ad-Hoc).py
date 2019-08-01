##Tristan Dufault 2019-08-01
##https://www.urionlinejudge.com.br/judge/en/problems/view/1612
import math

inp = int(input())

while(inp>0):

    inp2 = int(input())

    ans = math.ceil(inp2/2)
    print(ans)
    inp-=1
