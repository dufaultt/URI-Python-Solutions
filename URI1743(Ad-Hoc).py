##Tristan Dufault 2019-07-31
##Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1743

inp1 = input()
inp1l = inp1.split(" ")

inp2 = input()
inp2l = inp2.split(" ")

flag = 'true'

for i in range (5):
    if(inp1l[i] == inp2l[i]):
        flag = 'false'
        break

if(flag == 'true'):
    print('Y')
else:
    print('N')
