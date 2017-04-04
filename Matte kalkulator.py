import math
import string

print ('Her er lista med forskjellige kalkulatorar, skriv namnet på kalkulatoren du vil bruke.')
print ('Pythagoras')
print ('Forhold')
svar = input()
str.lower(svar)
if svar == 'pythagoras':
    svar = input('Vil du finne hypotenus eller ein katet? ')
    str.lower(svar)
    if svar == 'hypotenus':
        
        k1 = input ('Katet ')
        k2 = input ('Katet ')

        k1 = int(k1)
        k2 = int(k2)

        k1 = k1 ** 2
        k2 = k2 ** 2

        h = k1 + k2

        h = math.sqrt(h)

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

    a = input ('Skriv inn lengda på den eine kjende linja på den "ukjende" trekanten ')

    A = input ('Skriv inn lengda på linja som er lik X på motsatt trekant ')
    B = input ('Skriv inn lengda på linja på den "kjende" trekanten som er parallell til den du skreiv til den "ukjende" ')

    a = int (float(a))
    A = int (float(A))
    B = int (float(B))
    
    svar = a * A
    svar = svar / B

    print (svar)
else:
    print ('Vennligst skriv eit av alternativa')
