import math

def somma_due_numeri(a:float,b:float=5):
    '''questa funzione somma due numeri float e restituisce il loro risultato sommato'''
    somma = a+b
    print(somma)
    return somma

def area_quadrato(a):
    '''questa funzione calcola l'area del quadrato'''
    area = a*a
    return area

def area_rettangolo(a,b):
    '''questa funzione calcola l'area del rettangolo'''
    area = a*b
    return area


def area_triangolo(b,h):
    '''questa funzione calcola l'area del triangolo'''
    area = (b*h)/2
    return area


def area_cerchio(pi,r):
    '''questa funzione calcola l'area del cerchio'''
    area = pi * r ** 2
    return area


def area_sfera(pi,r):
    '''questa formula calcola l'area della sfera'''
    area = 4 * pi * r ** 2
    return area

def volume_sfera(pi,r):
    '''questa forumla calcola l'area della sfera'''
    volume = 4/3 * pi * r **2
    return volume

    
