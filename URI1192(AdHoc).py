#Tristan Dufault 2019/07/03

count = int(input())

while count>0:

    inp = input()
    inpl = list(inp)

    num1 = int(inpl[0])
    num2 = int(inpl[2])
    op = inpl[1]
    ans = 0

    if (num1 == num2):
        ans = num1*num2
    elif (op.isupper()):
        ans = num2-num1
    elif (op.islower()):
        ans = num1+num2

    print(ans)

    count -= 1
