##Tristan Dufault 2019-07-31
##Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1329

inp = input()


while(inp != '0'):

    inp2 = input()
    inpl = inp2.split(" ")
    lent = len(inpl)
    mar = 0
    jon = 0

    for i in range(lent):
        if(inpl[i] == '0'):
            mar += 1
        elif(inpl[i] == '1'):
            jon += 1

    print('Mary won {:d} times and John won {:d} times'.format(mar,jon))
    inp = input()
