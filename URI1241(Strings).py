#Tristan Dufault 2019-07-04

count = int(input())

while (count > 0):

    inp = input()
    inpl = inp.split(" ")
    num1 = inpl[0]
    num2 = inpl[1]
    flag = 0

    l1 = len(num1)
    l2 = len(num2)

    for i in range(l2):
        if(num1[l1-i-1] != num2[l2-i-1]):
            flag = 1
            break

    if (flag==1):
        print("nao encaixa")
    else:
        print("encaixa")



    count-=1
