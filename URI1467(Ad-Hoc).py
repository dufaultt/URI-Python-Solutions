#Tristan Dufault 2020-01-03
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1467

while True:
    try:
        inp = input()
        inpl = inp.split(" ")

        a = int(inpl[0])
        b = int(inpl[1])
        c = int(inpl[2])

        if((a==b) & (b==c)):
            print("*")
        elif((a==b) & (b!=c)):
            print("C")
        elif((a==c) & (b!=c)):
            print("B")
        elif((b==c) & (a!=c)):
            print("A")

    except EOFError:
        break
#end while
