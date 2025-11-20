# Adam Techman nr. alb. 73285
# Wstęp do programowania: Labolatorium 1

# Zadanie 1

print('\n__Zadanie 1:__')
print('A: (opisy operatorów w komentarzach w kodzie źródłowym)')
x = 1 + 2       #operator dodawania - dodaje wartosci, lub łączy ciągi znaków ; wynik w typie zmiennej int - liczba calkowita
print(type(x))  
x = 1 + 4.5     #operator dodawania ; wynik w typie zmiennej float - liczba zmiennoprzecinkowa
print(type(x))  
x = 3 / 2       #operator dzielenia - dzieli wartosci ; wynnik w zmiennej float
print(type(x))  
x = 4 / 2       #operator dzielenia ; wynik w zmiennej float?
print(type(x))  
x = 3 // 2      #operator dzielenia calkowitego ; wynik w zmiennej int
print(type(x))
x = -3 // 2     #operator dzielenia calkowitego ; wynik w zmiennej int
print(type(x))
x = 11 % 2      #operator modulo - wyswietla reszte z dzielenia : wynik w zmiennej int
print(type(x))
x = 2 ** 10     #operator potęgowania ; wynik w zmiennej int
print(type(x))
x = 8 ** (1/3)  #operator potęgowania ; wynik w zmiennej float
print(type(x))

print('B:')
print("Odpowiedzi do zadania 1B są zakomentowane w kodzie źródłowym")

# int(3.0) - zamienia zmienną typu float na typ integer - liczby zmiennoprzecinkowe na liczby całkowite
# float(3) - zamienia zmienną typu int na typ float - liczby całkowite na liczby zmiennoprzecinkowe
# float("3") - zamienia zmienną typu string na typ float - ciąg znaków na liczby zmiennoprzecinkowe
# str(12.4) - zamienia zmienną typu zmiennoprzecinkowej na ciąg znaków
# bool(0) - sprawdzenie wartości true/false (prawdziwości) danego wyrażenia, w przypadku 0 jest to false



# Zadanie 2

print('\n__Zadanie 2:__')

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)



# Zadanie 3

print('\n__Zadanie 3:__')

imię = 'Jan'
wiek = 20
wzrost = 178

print(f"Nazywam się {imię} i mam {wiek} lat.\n\nMój wzrost to {wzrost}cm.")



# Zadanie 4

print('\n__Zadanie 4:__')

Cena = 39.99
Rabat = 0.2

Cena = Cena * (1-Rabat)

print(round(Cena,2))



# Zadanie 5

print('\n__Zadanie 5:__')

a = float(input("Podaj wartość boku a: "))
b = float(input("Podaj wartość boku b: "))

pole = a*b
obwod = a+a+b+b

print(f"Pole prostokąta wynosi {pole}, a obwód {obwod}.")



# Zadanie 6

print('\n__Zadanie 6:__')


import random


# droga = float(input("Podaj pokonaną drogę. (w kilometrach): "))
# spalanie = float(input("Podaj średnie spalanie pojazdu. (l/100km): "))

# cena_paliwa = 6.5 #zl/l
# zuzycie = (droga/100) * spalanie
# koszt = zuzycie * cena_paliwa

# print(f"Koszt podróży wynosi {round(koszt,2)}zł, w której wykorzystano {round(zuzycie,2)} litrów paliwa.")

droga = random.randint(10,1000)
spalanie = float(input("Podaj średnie spalanie pojazdu. (l/100km): "))
cena_paliwa = float(input("Podaj cenę paliwa. (zł/l): "))

zuzycie = (droga/100) * spalanie
koszt = zuzycie * cena_paliwa

print(f"Koszt podróży wynosi {round(koszt,2)}zł, w której wykorzystano {round(zuzycie,2)} litrów paliwa na trasie {droga} kilometrów.")