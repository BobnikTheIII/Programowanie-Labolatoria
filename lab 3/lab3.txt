# Adam Techman 73285
# Programowanie: Labolatoria 3

# 1

print("Zadanie 1")

paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(paliwo,czas)
    paliwo = paliwo - paliwo_zużyte_na_s
    czas = czas + 1

print(paliwo,czas)

# 2

print("Zadanie 2")

liczba_bad = 3
liczby_pierwsze = [2]

while len(liczby_pierwsze) < 10:
    dzielnosc = False
    for i in range(2,liczba_bad):
        if liczba_bad % i == 0:
            dzielnosc = True
    
    if dzielnosc == False:
        liczby_pierwsze.append(liczba_bad)
    
    liczba_bad = liczba_bad + 1

print(liczby_pierwsze)


# 3

print("Zadanie 3")

ulice = ['Jagodowa','Lipowa','Kwiatowa','Kasztanowa','Polna']

for ulica in ulice:
    for i in range(6):
        for j in range(11):
            print(ulica,i,j)



# 5

print("Zadanie 5")

for i in range(80,-1,-4):
    print(i)


# 6

print("Zadanie 6")

a=0
while a > -1:
    a = int(input("Podaj liczbe: "))

# 8

print("Zadanie 8")

tekst = "Python jest super"

print(f"Zerowy indeks: {tekst[0]}")
print(f"Ostatni indeks: {tekst[-1]}")
print(f"Co drugi, zaczynając od zerowego: {tekst[::2]}")
print(f"Co trzeci, zaczynając od pierwszego: {tekst[1::3]}")
print(f"Od dziesiątego do ostatniego: {tekst[10:]}")
print(f"Od końca do początku: {tekst[::-1]}")

# 9

print("Zadanie 9")

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
print(f"Pierwsza połowa pierwszego łańcucha: {polowa1}")
