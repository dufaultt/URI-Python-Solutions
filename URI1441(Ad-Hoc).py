#Tristan Dufault 2020-01-13
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1441 

n = int(input()) 


while (n != 0):
    ans = 1
    n1 = 0
    while(n != 1):

        if(n > ans):
            ans = n
        #end if

        if(n % 2) == 0:
            n1 = int(n/2)
        else:
            n1 = (n*3)+1
        #end if
        n = n1

    #end while
    print(ans)
    n = int(input())
#end while
