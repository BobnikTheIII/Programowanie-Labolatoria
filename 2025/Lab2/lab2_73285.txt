# 1

print(" Zadanie 1")

tekstOdwrStudenta = int(input("Podaj tekstOdwr z egzaminu: "))

if tekstOdwrStudenta > 80:
    print("Gratulacje! Zdałeś egzamin.")
elif tekstOdwrStudenta >= 50:
    print("Gratulacje! Zdałeś egzamin. Możesz jednak poprawić jego tekstOdwr w następnym terminie.")
else:
    print("Nie zdałeś.")


# 2

print(" Zadanie 2")

x = int(input("Podaj wartość zmiennej x: "))
y = int(input("Podaj wartość zmiennej y: "))
z = int(input("Podaj wartość zmiennej z: "))

if x<=y<=z:
    print(f"{x}, {y}, {z}")
elif x<=z<=y:
    print(f"{x}, {z}, {y}")
elif z<=x<=y:
    print(f"{z}, {x}, {y}")
elif z<=y<=x:
    print(f"{z}, {y}, {x}")
elif y<=z<=x:
    print(f"{y}, {z}, {x}")
elif y<=x<=z:
    print(f"{y}, {x}, {z}")
else:
    print("Błąd")


# 3

print(" Zadanie 3")

Nazwa_pliku = "Raport_maj.xlsx"
odp=Nazwa_pliku.endswith(".xlsx")
if odp:
    print("Tak")
else:
    print("Nie")

# 4

print(" Zadanie 4")

gol = int(input("Podaj ilość zdobytych bramek: "))
bonus = 0

if gol > 10:
    bonus = 10
elif gol > 5:
    bonus = 5

print(f"Ostateczny tekstOdwr drużyny to {gol * 10 + bonus}")


# 5

print(" Zadanie 5")

with open("notowania_gieldowe.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip())

with open("notowania_gieldowe.txt", "a", encoding="utf-8") as plik:
    plik.write("ALR, 113\n")

print("\nNotowania po zmianie w piku: \n")
with open("notowania_gieldowe.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip())


# 6

print(" Zadanie 6")

litera = str(input("Podaj litere do sprawdzenia: "))

if  'A' <= litera <= 'Z' :
    print("Litera jest duża.")
elif  'a' <= litera <= 'z' :
    print("Litera jest mała.")
else:
    print("Błędna litera")


# 7

print(" Zadanie 7")

hasło = 'pk47!jy0893'
poprawnosc = False

for znak in hasło:
    if znak == "!" and len(hasło) >= 11:
        poprawnosc = True

if poprawnosc:
    print("Hasło jest poprawne.")
else:
    print("Hasło NIE jest poprawne.")


# 8

print(" Zadanie 8")

text = "Studiuje-informatykę"

print(f"Pierwsze trzy znaki ciągu: {text[0:3]}, ostatnie dwa znaki ciągu: {text[-2:]}")


# 9

print(" Zadanie 9")

tekst = input("Podaj tekst: ")
tekstOdwr = ""

for znak in tekst:
    if 'a' <= znak <= 'z':
        tekstOdwr += chr(ord(znak) - 32)
    elif 'A' <= znak <= 'Z':
        tekstOdwr += chr(ord(znak) + 32)
    else:
        tekstOdwr += znak

print(tekstOdwr)
