nr1 = float(input("Va rugam introduceti primul numar>> "))
alegeri = input("Alegeti o operatie: \n1. Adunare \n2. Scadere \n3. Inmultire \n4. Impartire \n ")
nr2 = float(input("Va rugam introduceti al doilea numar>> "))
dictionar_alegeri = {1 : "+" , 2 : "-", 3 : "*", 4 : "/"}
lista_alegeri = []
for key, value in dictionar_alegeri.items():
    if int(alegeri) == key:
        print(f"Se va efectua {nr1} {value} {nr2}")
rezultat = None
if alegeri == "1":
    rezultat = nr1 + nr2
elif alegeri == "2":
    rezultat = nr1 - nr2
elif alegeri == "3":
    rezultat = nr1 * nr2
elif alegeri == "4":
    if nr1 != 0 and nr2 != 0:
        rezultat = nr1 / nr2
    else:
        print("Impartirea cu 0 nu se poate face!!!")
        rezultat = "Operatia nu a putut fi efectuata"
else:
    print("Introduceti o valoare intre 1 si 4")

print(f"Rezultatul este: {rezultat}")



