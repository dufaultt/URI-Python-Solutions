#Tristan Dufualt 2019-07-08
count = int(input())

enum = []
onum = []

while (count>0):

    num = int(input())
    if (num%2 == 0):
        enum.append(num)
    else :
        onum.append(num)
    count-=1
#end while

ans = []

enum.sort()
onum.sort(reverse = True)
ans = enum + onum

size = len(ans)

for i in range(size):
    print(ans[i])
#end for
