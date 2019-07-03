#Tristan Dufault 2019-07-03

count = int(input())

while (count > 0):

    ans = input().split()
    ans.sort(key=len, reverse=True)

    for i in range(len(ans)):
        print(ans[i], end = '')
        if i != len(ans)-1:
            print(' ', end = '')
    print()

    count -= 1
