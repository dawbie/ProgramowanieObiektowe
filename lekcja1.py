'''
print("Hello World!!!")
print("Dzisiaj ",end='')
print("jest ",end='')
print("czwartek")

print("jestem ",end='\n')
print("na zajęciach ",end='')
print("z PO")

print(1)
print("2")
print(1+2)
print('1'+'2')
print(str(1)+'2')
print(1+int("2"))

print("Dzisiaj jest ",25,'kwietnia')

tekst="zmienna"
print(tekst)
tekst_zklawy=input("podaj tekst: ")
print(tekst_zklawy)
liczba_zklawy=int(input("podaj tekst: "))
print(liczba_zklawy*10)
'''
#kalkulator
'''
liczba1=int(input("podaj 1 liczbę"))
liczba2=int(input("podaj 2 liczbę"))
dzialanie = input("podaj dzialanie")
if dzialanie == "-":
    print(liczba1 - liczba2)
elif dzialanie == "+":
    print(liczba1 + liczba2)
elif dzialanie == "*":
    print(liczba1 + liczba2)
elif dzialanie == "/":
    print(liczba1 + liczba2)
    if liczba2 != 0:
        print(liczba1 / liczba2)
    else:
        print("nie dziel przez 0")
'''
# liczba1=int(input("podaj 1 liczbę"))
# liczba2=int(input("podaj 2 liczbę"))
# liczba3=int(input("podaj 3 liczbę"))
# if liczba1>liczba2 and liczba1 > liczba3:
#         print("liczba ",liczba1," jest największa")
# elif liczba2>liczba1 and liczba2>liczba3:
#         print("liczba ",liczba2," jest największa")
# else:
#     print("liczba ",liczba3," jest najwieksza")
#
    #koniec ćwiczeń

znaki= ['+','-','/','*']
dzialanie=str(input("podaj działanie"))#321-2
i=0
j=0
znak='+'
wynik = 0
liczba1=0
liczba2=0

while j < len(dzialanie):
    if dzialanie[j] in znaki:
        liczba1=int(dzialanie[i:j])
        znak=dzialanie[j]
        j += 1
        i = j
        continue
    else:
        j+=1
        # print('else')
        # print(j)
        continue
liczba2=int(dzialanie[i:j])
if znak == "+":
    wynik = liczba1+liczba2
elif znak == "-":
    wynik = liczba1-liczba2
elif znak == "*":
    wynik = liczba1*liczba2
elif znak == "/":
    if liczba2 == 0:
        wynik=0
    else:
        wynik = liczba1/liczba2
else:
    print('błędny znak')
print(wynik)



