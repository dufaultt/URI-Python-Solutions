#Tristan Dufault 2020-01-09
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1216

count = 0
aggr = 0


while True:
    try:

        inpx = input()
        aggr = aggr + int(input())
        count += 1

    except EOFError:
        break
#end while

ans = float(aggr)/count
print('{:0.1f}'.format(ans))
