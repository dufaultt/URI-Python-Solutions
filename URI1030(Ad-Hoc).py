#Tristan Dufault -Work in progress
#Problem link: https://www.urionlinejudge.com.br/judge/en/problems/view/1030
iterate = int(input())
num = 1

while(iterate > 0):
    ans = 0
    flag = 0
    i = 0
    cyc = 0
    deaths = 0
    inp = input()
    inpl = inp.split(" ")

    total = int(inpl[0])
    step = int(inpl[1])
    circle = [0]*total

    for i in range(total):
        circle[i] = i+1
    #end for

    while(flag == 0):

        i+=1
        if(i == len(circle)):
            i = 0
        #end if

        if(circle[i] != 0):
            cyc +=1
        #end if
        if(cyc == step):
            circle[i] = 0
            deaths+=1
            cyc = 0
        #end if

        if(deaths == (total-1)):
            flag = 1
        #end if
    #end while
    for i in range(len(circle)):
        if(circle[i] != 0):
            ans = i+1
        #end if
    #end for
    print('Case {:d}: {:d}'.format(num, ans))
    num+=1
    iterate-=1
#end while
