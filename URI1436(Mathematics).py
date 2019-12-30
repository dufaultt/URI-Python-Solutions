#Tristan Dufault 2019-12-30
#Problem link: https://www.urionlinejudge.com.br/judge/en/problems/view/1436
iterate = int(input())
num = 1

while(iterate > 0 ):
    inp = input()
    inpl = inp.split(" ")
    inpl = list(map(int, inpl))

    inpl.sort()
    l = len(inpl)
    m = int(l/2)

    print('Case {:d}: {:d}'.format(num,inpl[m]))

    num+=1
    iterate-=1
#end while
