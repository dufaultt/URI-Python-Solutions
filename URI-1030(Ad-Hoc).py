#Tristan Dufault -work in progress
#Problem link: https://www.urionlinejudge.com.br/judge/en/problems/view/1030
iterate = int(input())
num = 1

while(iterate > 0):
    ans = 0
    inp = input()
    inpl = inp.split(" ")

    total = int(inpl[0])
    step = int(inpl[1])
    circle = [0]*total

    for i in range(total):
        circle[i] = i+1
    #end for

    print(circle)
    print('Case {:d}: {:d}'.format(num, ans))
    num+=1
    iterate-=1
#end while
