##Tristan Dufault 2019/06/28

count = int(input())

while(count > 0):

    x = int(input())
    y = 2**x

    z = int(y/12000)
    print('{:d} kg'.format(z))
    count-= 1
