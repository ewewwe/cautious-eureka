poäng=0
n=0
f=0
def kontrollera_gissning(gissning,svar):
    global n
    if gissning.lower() == svar.lower():
        global poäng
        print('Rätt svar')
        if n == 0 or n == 3 or n == 6:
            poäng=poäng+3
        elif n == 1 or n == 4 or n == 7:
            poäng=poäng+2
        else:
            poäng=poäng+1
        if n <= 2:
            n=3
        elif n > 2 and n <= 5:
            n=6
        else:
            n=9
            f=9
    else:
        print('Tyvärr det var fel försök igen')
        n=n+1
        return n 
print('Gissa Djuret:')
while f < 9:
    if n <= 2:
        gissning1=input('Vilket djur bor på Nordpolen?')
        kontrollera_gissning(gissning1,'isbjörn')
    elif n > 2 and n <= 5:
        gissning1=input('Vilket är det snabbaste landdjuret?')
        kontrollera_gissning(gissning1,'gepard')
    elif n > 5 and n <= 8:
        gissning1=input('Vilket är det största djuret?')
        kontrollera_gissning(gissning1,'blåval')
    else:
        f=9
        print('Din poäng är '+str(poäng))



