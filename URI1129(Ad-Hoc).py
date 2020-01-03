#Tristan Dufault 2020-01-03
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1129

inp = int(input())

while (inp != 0):
    iter = inp


    while(iter>0):
        inp = input()
        ans = "a"
        inpl = inp.split(" ")
        inpl = list(map(int, inpl))
        flag = 0
        size = len(inpl)

        for i in range(size):
            if(inpl[i]<128):
                flag+=1
                if(i==0):
                    ans = 'A'
                elif(i==1):
                    ans = 'B'
                elif(i==2):
                    ans = 'C'
                elif(i==3):
                    ans = 'D'
                elif(i==4):
                    ans = 'E'
            #end if
        #end for
        if(flag==1):
            print(ans)
        else:
            print("*")
        #end if

        iter-=1

    #end while

    inp = int(input())

#end while
