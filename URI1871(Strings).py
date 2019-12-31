#Tristan Dufault 2019-12-30
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1871

inp = input()
inpl = inp.split(" ")
inpl = list(map(int, inpl))

while((inpl[0]+inpl[1]) != 0):

    s = inpl[0]+inpl[1]
    ls = [int(x) for x in str(s)]
    size = len(ls)

    try:
        for i in range(100):
            ls.remove(0)
    except:
        a = 0
    #end try/except

    ans = int("".join(map(str, ls)))
    print(ans)

    inp = input()
    inpl = inp.split(" ")
    inpl = list(map(int, inpl))
#end while
