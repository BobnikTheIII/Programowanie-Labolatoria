# Adam Techman 73285
# Wstęp do programowania : Labolatorium 4 


# 1

print(" Zadanie 1")


Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

m = 1
n = 4
k = -1
i = 2

Moja_lista1 = "AAAAAA"
Moja_lista2 = "BBBBBB"

Moja_lista=[1, 2, 3, 4]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[0]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[-1]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

len(Moja_lista)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

max(Moja_lista)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

min(Moja_lista)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

sum(Moja_lista)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

sorted(Moja_lista)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista.append(6)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista.insert(i,5)
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista.pop()
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista.reverse()
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista = Moja_lista1 + Moja_lista2
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista = Moja_lista1*5
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[ :n]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[m: ]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[m:n:k]
print(Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista[::-1]
print(Moja_lista)


# 2

print(" Zadanie 2")

obywatele = ["Krzysztof","Michał","Jakub","Tomasz"]

print("a)")

obywatele.sort()

print(obywatele)

print("b)")

obywatele.append("Mieszko")
obywatele.append("Świętosław")

print(obywatele.pop())
print(obywatele.pop())

print("c)")

obywatele.insert(2,"Kunegunda")
print(obywatele)

print("d)")

obywatele2 = obywatele
print(obywatele.reverse())


# 3

print(" Zadanie 3")

imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}!")

wiek = int(input("Podaj swój wiek: "))
print(f"Twój wiek to: {wiek}")

imie, nazwisko = input("Podaj swoje imię i nazwisko: ").split()
print(f"Inicjały: {imie[0].upper()}.{nazwisko[0].upper()}.")

lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print(f"Połączony łańcuch: {lancuch3}")

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polowa1 = lancuch1[:len(lancuch1)//2]
polowa2 = lancuch2[len(lancuch2)//2:]
print(f"Powstały łańcuch: {polowa1} {polowa2}")



# 5

print(" Zadanie 5")

krotka = ("Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela")

print(krotka)



# 6

print(" Zadanie 6")

owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')

licz_banan = 0

for owoc in owoce:
    if owoc == "banan":
        licz_banan =+ 1

print(f"W krotce banan zawiera się {licz_banan} raz(y)")


# 7

print(" Zadanie 7")

moja_krotka = (10, 2, 6, 6, 9, 13, 0,1)

temp = list(moja_krotka)

temp.sort()

moja_krotka = tuple(temp)

print(moja_krotka)



# 8

print(" Zadanie 8")

stopnie = (
"Szeregowy",
"Kapral",
"Sierżancie",
"Porucznik",
"Kapitan",
"Major",
"Pułkownik",
)

ilosc_stopni = len(stopnie)
print(ilosc_stopni)
Major_index = stopnie.index("Major")
print(Major_index)
Pułkownik_wstepowanie = "Pułkownik" in stopnie
print(Pułkownik_wstepowanie)


# 9

print(" Zadanie 9")

lista_zakupow = {
    'bulka' : 0.69,
    'mleko' : 4.99,
    'woda' : 2.49
}

suma=0

for przedmiot in lista_zakupow:
    suma += lista_zakupow[przedmiot]

print(f'Lista zakupów: {lista_zakupow}. Łączna suma wydatków: {suma}')