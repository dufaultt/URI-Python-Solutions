##Tristan Dufault 2019-08-02
##Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1387

inp = input()
inpl = inp.split(" ")

while((inpl[0] != '0') and (inpl[1] != '0')):
    ans = int(inpl[1])+int(inpl[0])
    print(ans)

    inp = input()
    inpl = inp.split(" ")
