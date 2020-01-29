#Tristan Dufault 2020-01-23
#Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1763 

countrlist = ['brasil','alemanha','austria','coreia','espanha','grecia','estados-unidos','inglaterra','australia','portugal','suecia','turquia','argentina','chile','mexico','antardida','canada','irlanda','belgica','italia','libia','siria','marrocos','japao']
greetlist = ['Feliz Natal!','Frohliche Weihnachten!','Frohe Weihnacht!','Chuk Sung Tan!','Feliz Navidad!','Kala Christougena!','Merry Christmas!','Merry Christmas!','Merry Christmas!','Feliz Natal!','God Jul!','Mutlu Noeller','Feliz Navidad!','Feliz Navidad!','Feliz Navidad!','Merry Christmas!','Merry Christmas!','Nollaig Shona Dhuit!','Zalig Kerstfeest!','Buon Natale!','Buon Natale!','Milad Mubarak!','Milad Mubarak!','Merii Kurisumasu!']

lenc = len(countrlist)
leng = len(greetlist) 
 

while True:
    try:
        inp = input()
        flag = 0

        for i in range(lenc):
            if(countrlist[i] == inp):
                print(greetlist[i])
                flag = 1
                break
            #end if
        #end for

        if (flag == 0):
            print('--- NOT FOUND ---')
        #end if

    except EOFError:
        break
#end while
