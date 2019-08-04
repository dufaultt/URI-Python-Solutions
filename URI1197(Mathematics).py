##Tristan Dufault 2019/06/28
##Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1197

while True:
    try:
        inp = input()
        inpl = inp.split(" ")

        x = int(inpl[0])
        y = int(inpl[1])

        z = x*y*2

        print(z)
    except EOFError:
        break
