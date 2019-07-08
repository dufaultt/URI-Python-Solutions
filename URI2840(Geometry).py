#Tristan Dufualt 2019-07-08
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/2840
#V = (4/3)pi*r^3

inp = input()
inpl = inp.split(" ")

r = int(inpl[0])
l = int(inpl[1])

ans = (4/3)*3.1415*(r**3)

num = int(l/ans)

print(num)
