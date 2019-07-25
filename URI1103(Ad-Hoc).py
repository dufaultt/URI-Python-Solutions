##Tristan Dufault 2019-07-25
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1103

inp = input()
inpl = inp.split(" ")

while((inpl[0] != '0') or (inpl[1] != '0') or (inpl[2] != '0') or (inpl[3] != '0')):

    h1 = int(inpl[0])
    h2 = int(inpl[2])
    m1 = int(inpl[1])
    m2 = int(inpl[3])

    ansh=0
    ansm=0
    anst=0

    if(h1>h2):
        ansh = (24-h1) + (0+h2)
    elif((h1==h2) & (m1>m2)):
        ansh = 24
    else:
        ansh = h2-h1

    ansm = m1-m2

    anst = (ansh*60) - ansm

    print(anst)

    inp = input()
    inpl = inp.split(" ")
