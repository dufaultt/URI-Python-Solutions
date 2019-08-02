##Tristan Dufault 2019-08-01
##https://www.urionlinejudge.com.br/judge/en/problems/view/1235

iter = int(input())

while(iter>0):

    s = input()
    sl = list(s)
    hsl = sl.copy()
    half = (int(len(sl)/2))-1
    
    if((len(sl)%2) >0):
        for i in range(half+1):
            sl[i] = hsl[half-i]

        for i in range(int(len(sl)/2)+1,len(sl)):
            sl[i] = hsl[len(sl)+(int(len(sl)/2))-i]

    else:
        for i in range(half+1):
            sl[i] = hsl[half-i]

        for i in range(half+1,len(sl)):
            sl[i] = hsl[len(sl)+half-i]

    ans = ''.join(sl)
    print(ans)
    iter-=1
