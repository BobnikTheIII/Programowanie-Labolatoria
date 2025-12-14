# 1

print("Zadanie 1")

def kwadratLiczby(m):
    m = m * m
    print(f"Kwadrat podanej liczby wynosi {m}.")

kwadratLiczby(5)

# 2

print("Zadanie 2")

def revString(string):
    string = string[::-1]

revString("testowy string")

# 3



print("Zadanie 3")

def powitanie(imie="Użytkowniku",jezyk="polski"):
    
    if jezyk == "polski":
        print(f"Cześć {imie}!")
    elif jezyk == "angielski":
        print(f"Hello {imie}!")
    elif jezyk == "niemiecki":
        print(f"Guten tag {imie}!")
    else:
        print(f"Witaj {imie}")


powitanie("Adam","włoski")

# 4

print("Zadanie 4")

def srednia(liczby):
    suma = 0
    for liczba in liczby:
        suma = suma + liczba

    print(f"Średnia = {suma/liczby.len}")

srednia([6,4,3,6,2,6])



# 5

print("Zadanie 5")

def BMI(masa,wzrost):
    print(f"BMI to {masa / (wzrost*wzrost)}")

BMI(70,1.6)



# 6

print("Zadanie 6")

def heron(a,b,c):
    p=(a+b+c)/2

    print(f"Pole trojkata wynosi {(p*(p-a)*(p-b)*(p-c))**(1/2)}")

heron(2,4,5)



# 7

print("Zadanie 7")

def potegowanie(podstawa,wykladnik,i=0):
    print(f"Potęga o podstawie {podstawa} i wykładniku {wykladnik} wynosi {podstawa**wykladnik}.")

    
    if i<wykladnik: potegowanie(podstawa,wykladnik,i+1)


potegowanie(2,4)



# 8

print("Zadanie 8")

def najwiekszyParametr(*p):
    max = p[0]
    for i in p:
        if i > max:
            max = i

    print(f"Największy parametr to {max}.")

najwiekszyParametr(3,6,2,8,4,1)



# 9

print("Zadanie 9")

def ciagFibonacciego(n):
    a,b = 0,1
    wynik = []
    for _ in range(n):
        wynik.append(a)
        a,b = b,a+b

    print(f"Ciag Fibonacciego dla n={n} to: {wynik}")