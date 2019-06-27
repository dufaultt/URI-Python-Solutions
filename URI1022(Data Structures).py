##Tristan Dufault 06/27/2019

from fractions import gcd

count = int(input())

while (count > 0):

    inp = input()
    inpl = inp.split(" ")

    N1 = int(inpl[0])
    D1 = int(inpl[2])
    op = inpl[3]
    N2 = int(inpl[4])
    D2 = int(inpl[6])


    div = 0;

    if (op == '+'):
        ans1n = ((N1*D2) + (N2*D1))
        ans1d = (D1*D2)
    elif (op == '-'):
        ans1n = ((N1*D2) - (N2*D1))
        ans1d = (D1*D2)
    elif (op == '*'):
        ans1n = (N1*N2)
        ans1d = (D1*D2)
    elif (op == '/'):
        ans1n = (N1*D2)
        ans1d = (N2*D1)

    div = gcd(ans1n, ans1d)
    ans2n = int(ans1n/div)
    ans2d = int(ans1d/div)

    print('{:d}/{:d} = {:d}/{:d}'.format(ans1n,ans1d,ans2n,ans2d))


    count-=1
