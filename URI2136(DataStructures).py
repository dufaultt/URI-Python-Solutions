#Tristan Dufault 2020-01-02
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/2136

namesy = []
namesn = []
win = 0
winn = 'a'

inp = input()


while (inp != 'FIM'):
    inpl = inp.split(" ")


    if(inpl[1] == 'YES'):
        if (inpl[0] not in namesy):
            namesy.append(inpl[0])
        #end if
        if(len(inpl[0]) > win):
            winn = inpl[0]
            win = len(inpl[0])
        #end if
    else:
        if (inpl[0] not in namesn):
            namesn.append(inpl[0])
        #end if
    #end if

    namesy.sort()
    namesn.sort()

    inp = input()
#end while

sizey = len(namesy)
for i in range(sizey):
    print(namesy[i])

sizen = len(namesn)
for i in range(sizen):
    print(namesn[i])

print("")
print("Amigo do Habay:")
print(winn)
