##Tristan Dufault 2019/06/28
##Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1214
 
iterate = int(input())

while(iterate > 0):

    iterate -= 1
    inp = input()
    inpl = inp.split(" ")
    sum = 0
    count = 0
    N = int(inpl[0])
    N1 = N

    while(N1 > 0):
        sum += int(inpl[N1])
        N1 -= 1

    avg = sum/N
    N1 = N

    while(N1 > 0):
        if(int(inpl[N1]) > avg):
            count+=1
        N1-=1

    perc = (count/N)*100

    print('{:.3f}%'.format(perc))
