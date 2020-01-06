#Tristan Dufault 2020-01-06
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1272

count = int(input())

while(count>0):
    inp = input()
    inpl = inp.split(" ")
    ans = []

    while('' in inpl):
        inpl.remove('')
    #end while

    size = len(inpl)

    for i in range(size):
        sval = inpl[i]
        cval = sval[:1]
        ans.append(cval)
    #end for
    count-=1

    sans = ""
    for i in ans:
        sans += i
    #end for
    
    print(sans)
#end while
