#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random
from pygame.locals import * #udostępnienie nazw metod z locals
import sys

import random



reload(sys)
sys.setdefaultencoding('utf-8')
# inicjacja modułu pygame
pygame.init()

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
OKNOGRY = pygame.display.set_mode((450, 450),0, 32)
# tytuł okna gry

pygame.display.set_caption('Sudoku')

# lista opisująca stan pola gry, 0 - pole puste, 1 - gracz, 2 - komputer
POLE_GRY = [0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,]


POZIOM = [ # trójki pól planszy do sprawdzania
        [0,1,2,3,4,5,6,7,8],
        [9,10,11,12,13,14,15,16,17],
        [18,19,20,21,22,23,24,25,26],
        [27,28,29,30,31,32,33,34,35],
        [36,37,38,39,40,41,42,43,44],
        [45,46,47,48,49,50,51,52,53],
        [54,55,56,57,58,59,60,61,62],
        [63,64,65,66,67,68,69,70,71],
        [72,73,74,75,76,77,78,79,80]
 ]


LOSOWANIE =  [ # trójki pól planszy do sprawdzania

        ]
for e in range(0,9):
    tmp1 = (random.randint(0, 80))
    LOSOWANIE.append(tmp1)

tmp = (random.randint(0, 9))
for y in LOSOWANIE:

    print LOSOWANIE
    #print 'poziom___'+str(y)
    while tmp in POLE_GRY:
        tmp = (random.randint(0, 9))
           # print 'wylosowana liczba '+str(tmp)
    print tmp
    #print tabela_chwilowa
    POLE_GRY[y] = tmp


POLE_GRY3 = [1,4,9,3,6,8,5,7,2,7,2,8,1,5,4,3,9,6,5,3,6,9,2,7,1,4,8,2,5,4,6,7,3,8,1,9,8,9,3,2,4,1,6,5,7,6,7,1,8,9,5,2,3,4,
9,8,5,7,3,6,4,2,1,3,1,2,4,8,9,7,6,5,4,6,7,5,1,2,9,8,3]

POLE_GRY2 = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,
             7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,8]

POLE_GRY1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,
             1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,8]


PION = [ # trójki pól planszy do sprawdzania
        [0,9,18,27,36,45,54,63,72],
        [1,10,19,28,37,46,55,64,73],
        [2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],
        [6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]

 ]



SPRAWDZENIE = [1, 2, 3, 4, 5, 6, 7, 8, 9]


X = 400
Y = 400
liczba = 1
wynik_gra = [[],[]]
def rysuj_plansze():
    for i in range(0,9):#x
        for j in range(0,9):#y
            # argumenty: powierzchnia, kolor, x,y, w,h, grubość linii
            pygame.draw.rect(OKNOGRY, (255,255,255), Rect((j*50,i*50),(50,50)), 1)




def rysuj_pole_gry():
    for i in range(0,9):
        for j in range(0,9):
            pole = i*9+j #zmienna pole przyjmuje wartości od 0-8
            # x i y określają środki kolejnych pól,
            # a więc wartości: 25,25, 25,75 25,125 75,25 itd.
            x = j*50+25
            y = i*50+25

            if POLE_GRY[pole] >= 0:
                font = pygame.font.Font('freesansbold.ttf', 32)
                tekst_obr = font.render(str(POLE_GRY[pole]), True, (255, 255, 20))
                tekst_prost = tekst_obr.get_rect()
                tekst_prost.center = (x, y)
                OKNOGRY.blit(tekst_obr, tekst_prost)




def wynik_ostateczny():

    print 'wynik: ' + str(wynik_gra)
    if sum(wynik_gra[0])==9 and sum(wynik_gra[1])==9:
        fontObj = pygame.font.Font('freesansbold.ttf', 50)
        tekst = u'KONIEC GRY!!!!'

        tekst_obr = fontObj.render(tekst, True, (20, 255, 20))
        tekst_prost = tekst_obr.get_rect()
        tekst_prost.center = (225, 225)
        OKNOGRY.blit(tekst_obr, tekst_prost)


def sprawdzenie_liczb(par):
    tablica = []
    #print par

    fik_tabela = []
    for i in range(0,9):
        for j in POZIOM[par]:
            if SPRAWDZENIE[i] == POLE_GRY[j]:

                tablica.append(1)

                fik_tabela.append(POLE_GRY[j])


    if dict([(x,fik_tabela.count(x)) for x in fik_tabela]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1} and sum(tablica) == 9:

        return True

def sprawdzenie_liczb1(par):
    tablica1 = []


    fik_tabela = []
    for i in range(0,9):
        for j in PION[par]:
            if SPRAWDZENIE[i] == POLE_GRY[j]:

                tablica1.append(1)

                fik_tabela.append(POLE_GRY[j])

    if dict([(x,fik_tabela.count(x)) for x in fik_tabela]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1} and sum(tablica1) == 9:

        return True



def sprawdz_wynik_poziom():
    suma = 0
    wynik_gra2 = []

    for i1 in range(0,9):
        for i in POZIOM[i1]: #wiersz
           # print 'i '+str(i)

            suma = suma + POLE_GRY[i]

            kolor= i1*50
        test = sprawdzenie_liczb(i1)


        if suma == 45 and test == True:
            wynik_gra2.append(1)
            wynik_gra[0] = (wynik_gra2)

            for i in range(0, 9):
                for j in range(0, 1):
                    x = j * 50+ kolor
                    y = i * 50
                    red = (255,0,0)
                    #wiersze liczyc co 30 pierwsza wartość
                    pygame.draw.rect(OKNOGRY,red,[y,x,50,50])
        suma = 0


def sprawdz_wynik_pion():
    suma = 0

    wynik_gra1 = []
    for i1 in range(0,9):
        for i in PION[i1]: #wiersz

            suma = suma + POLE_GRY[i]

            kolor= i1*50

        test = sprawdzenie_liczb1(i1)
       # print 'sprawdzenie_liczb1' + str(test)
        # print 'Suma:' +str(suma)

        if suma == 45 and test == True:
            wynik_gra1.append(1)
            wynik_gra[1] =(wynik_gra1)

            suma = 0

            for i in range(0, 1):
                for j in range(0, 9):
                    x = j * 50
                    y = i * 50 +kolor
                    red = (255,0,0)
                    #wiersze liczyc co 30 pierwsza wartość
                    pygame.draw.rect(OKNOGRY,red,[y,x,50,50])
        suma = 0


while True:
   # print 'aaa'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1: # jeżeli naciśnięto pierwszy przycisk

                print '<--------NOWY WPIS NA PLANSZY GRY------->'
                OKNOGRY.fill((0, 0, 0))
                liczba = liczba +1
                mouseX, mouseY = event.pos # rozpakowanie tupli
                pole = ((mouseY/50)*9)+(mouseX/50) # wylicz indeks klikniętego pola
                print pole

                if pole in LOSOWANIE:
                    print 'nie ruszaj'
                elif POLE_GRY[pole] < 9:
                    POLE_GRY[pole] = POLE_GRY[pole]+1
                    print 'pole gry w sekcji dodawania wpisów '+str(POLE_GRY)
                    wynik_gra = [[], []]
                elif POLE_GRY[pole] > 8:
                    POLE_GRY[pole] = 0
                    wynik_gra = [[],[]]

                #print POLE_GRY
                sprawdz_wynik_poziom()
                sprawdz_wynik_pion()
                wynik_ostateczny()
    rysuj_plansze()
    rysuj_pole_gry()

    pygame.display.update()
