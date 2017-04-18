import math

print ('Her er lista med forskjellige kalkulatorar, skriv namnet på kalkulatoren du vil bruke.')
print ('Pythagoras')
print ('Forhold')
print ('Sannsyn')

svar = input()
svar = str.lower(svar)
if svar == 'pythagoras':
    svar = input('Vil du finne hypotenus eller ein katet? ')
    str.lower(svar)
    if svar == 'hypotenus':
        svar = input ('Av ein pyramide eller ein trekant?')
        str.lower (svar)

        if svar == 'trekant':
            
            k1 = input ('Katet ')
            k2 = input ('Katet ')

            k1 = int(float (k1))
            k2 = int(float (k2))

            k1 = k1 ** 2
            k2 = k2 ** 2

            h = k1 + k2

            h = math.sqrt(h)

            print (h)
            
        elif svar == 'pyramide':
            
            k1 = input ('Lenga av ein side på botnplata ')
            k2 = input ('Høga på pyramiden ')

            k1 = int (float (k1))
            k2 = int (float (k2))

            k1 = k1 / 2

            k1 = k1 ** 2
            k2 = k2 ** 2

            h = k1 + k2

            h = math.sqrt (h)
            
            print (h)
        
    elif svar == 'katet':
        
        k1 = input ('Hypotenus ')
        k2 = input ('Katet ')

        k1 = int(k1)
        k2 = int(k2)

        k1 = k1 ** 2
        k2 = k2 ** 2

        h = k1 - k2

        h = math.sqrt(h)

        print (h)
        
elif svar == 'forhold':

    a = input ('1) Skriv inn lengda på den eine kjende linja på den "ukjende" trekanten ')

    A = input ('2) Skriv inn lengda på linja som er lik X på motsatt trekant ')
    B = input ('3) Skriv inn lengda på linja på den "kjende" trekanten som er parallell til den du skreiv til 1) ')

    a = int (float(a))
    A = int (float(A))
    B = int (float(B))
    
    svar = a * A
    svar = svar / B

    print (svar)

elif svar == 'sannsyn':
    Gunstige = input ('Skriv inn antall gunstige utfall ')
    Moglege = input ('Skriv inn antall moglege utfall ')

    Gunstige = int (float (Gunstige))
    Moglege = int (float (Moglege))

    svar = Gunstige / Moglege

    svar = str (svar)

    print ('Sannsynet for eit gunstigt utfall er ' + svar)

else:
    print ('Vennligst skriv eit av alternativa')
