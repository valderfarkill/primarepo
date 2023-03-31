#area quadrato
def area_quadrato(a):
    area = a*a
    return area

ris = area_quadrato(int(input("il numero inserito è ")))
print(ris)

#perimetro quadrato
def perimetro_quadrato(a):
    perimetro = a*4
    return perimetro

ris = perimetro_quadrato(int(input("il numero inserito è ")))
print(ris)


#area rettangolo
def area_rettangolo(a,b):
    area = a*b
    return area

input1 = int(input("il primo valore è "))
input2 = int(input("il secondo valore è "))
ris = area_rettangolo(input1,input2)
print(ris)

#perimetro rettangolo
def perimetro_rettangolo(a,b):
    perimetro = (a*2)+(b*2)
    return perimetro

input1 = int(input("il primo valore è "))
input2 = int(input("il secondo valore è "))
ris = perimetro_rettangolo(input1,input2)
print(ris)


#area triangolo
def area_triangolo(b,h):
    area = (b*h)/2
    return area

input1 = int(input("il primo valore è "))
input2 = int(input("il secondo valore è "))
ris = area_triangolo(input1,input2)
print(ris)

#perimetro triangolo
def perimetro_triangolo(a,b,c):
    perimetro = a+b+c
    return perimetro

input1 = int(input("il primo valore è "))
input2 = int(input("il secondo valore è "))
input3 = int(input("il terzo valore è "))
ris = perimetro_triangolo(input1,input2,input3)
print(ris)

def tipo_di_triangolo(a,b,c):
    if a == b == c:
        return ("equilatero")
    elif a == b or b == c or a == c:
        return("isoscele")
    else:
        return("scaleno")

print(f"il triangolo è {tipo_di_triangolo(input1,input2,input3)}")

#area cerchio
def area_cerchio(pi, r):
    area = pi * r ** 2
    return area
input1 = float(input("il primo valore è "))
input2 = float(input("il secondo valore è "))
ris = area_cerchio(input1,input2)
print(ris)
    
