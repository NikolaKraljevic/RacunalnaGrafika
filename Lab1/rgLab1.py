import pyglet
import numpy as np
from pyglet.gl import *
from pyglet.window import key

pomak = 45
povecanje = 10

#Ovdje cemo racunati aproksimacijsku i tangentu
def IzracunajBSplineMatrice(lista_putanje,ri,t):
    T3 = np.array([pow(t,3),pow(t,2),t,1])
    B3 = 1/6 * np.array([[-1,3,-3,1],[3,-6,3,0],[-3,0,3,0],[1,4,1,0]])
    kopija_liste = lista_putanje
    R = np.array([kopija_liste[ri-1],kopija_liste[ri],
                  kopija_liste[ri+1],kopija_liste[ri+2]])
    TB = np.dot(T3,B3)
    #Dobiveno rjesenje za aproksimacijsku unfiformnu krivulju
    TBR = np.dot(TB,R)

    T2 = np.array([pow(t,2),t,1])
    Bd3 = 1/2 * np.array([[-1,3,-3,1],[2,-4,2,0],[-1,0,1,0]])

    tanTB = np.dot(T2,Bd3)
    tanTBR = np.dot(tanTB,R)
    print (TBR)
    return TBR,tanTBR

def IzracunajBSpline():
    global lista_putanje
    lista_putanje = []
    file_put = open("bspline.obj")

    for line in file_put:
        elements = line.split()
        lista_putanje.append((float(elements[1]), float(elements[2]), float(elements[3]), 1))

    x_max,x_min = float(-9999999999),float(999999999)
    y_max,y_min = float(-9999999999),float(999999999)
    z_max,z_min = float(-9999999999),float(999999999)

    for tocka in lista_putanje:
        x_max = max(x_max,tocka[0])
        x_min = min(x_min,tocka[0])
        y_max = max(y_max,tocka[1])
        y_min = min(y_min,tocka[1])
        z_max = max(z_max,tocka[2])
        z_min = min(z_min,tocka[2])

    centar_x = (x_min+x_max)/2
    centar_y = (y_max+y_min)/2
    centar_z = (z_max+z_min)/2

    razlika_x = x_max-x_min
    razlika_y = y_max-y_min
    razlika_z = z_max-z_min
    razlika = max(razlika_x,razlika_y,razlika_z)
    tocka = []
    tangenta = []
    za_t = np.linspace(0,1,20)
    for i in range(1,len(lista_putanje)-2):
        for t in za_t:
            tockat,tangentat = IzracunajBSplineMatrice(lista_putanje,i,t)
            tocka.append(tockat)

            tangenta.append(tangentat)

    for i in range(178):
        j = i+1
        
        medo.add(2,GL_POINTS, None, ('v2f', (
        (tocka[i][0] + pomak) * povecanje, (tocka[i][1] + pomak) * povecanje, (tocka[j][0] + pomak) * povecanje,
        (tocka[j][1] + pomak) * povecanje)), ('c3B', (255, 255, 255, 255, 255, 255)))


        medo.add(2,GL_POINTS, None, ('v3f', (
        (tocka[i][0] + pomak) * povecanje, (tocka[i][1] + pomak) * povecanje,(tocka[i][2]+pomak)*povecanje, (tocka[j][0] + pomak) * povecanje,
        (tocka[j][1] + pomak) * povecanje,(tocka[j][2]+pomak)*povecanje)), ('c3B', (255, 255, 255, 255, 255, 255)))


        medo3.add(2, GL_LINE_STRIP, None, ('v2f', (
            (tocka[i][0] + pomak) * povecanje, (tocka[i][1] + pomak) * povecanje,
            (tocka[i][0] + pomak + tangenta[i][0]) * povecanje,
            (tocka[i][1] + pomak + tangenta[i][1]) * povecanje)), ('c3B', (255, 255, 255, 255, 255, 255)))


    return tocka,tangenta



lista_tocaka_poligona = []
lista_poligona = []
#cita samo medu i takvi su parametri
file = open('teddy.obj')

window = pyglet.window.Window(1000, 1000)
for line in file:
    #splitamo liniju i provjeravamo nulti i onda odredimo di kaj ide
    try:
        elements = line.split()
        if elements[0] is 'v':
            lista_tocaka_poligona.append((float(elements[1]), float(elements[2]), float(elements[3]),1))
        if elements[0] is 'f':
            lista_poligona.append((int(elements[1]) - 1, int(elements[2]) - 1, int(elements[3]) - 1))
    except:
        nista = 0
global brojac_tocki
brojac_tocki = 1
medo = pyglet.graphics.Batch()

medo3 = pyglet.graphics.Batch()

tocka,tangenta = IzracunajBSpline()



def Crtaj(brojac_tocki):
    global medo5
    print(tocka[10])

    if(brojac_tocki<180):
        medo5 = pyglet.graphics.Batch()
        for i in range(len(lista_poligona)):
            tocka1 = lista_tocaka_poligona[lista_poligona[i][0]]


            tocka2 = lista_tocaka_poligona[lista_poligona[i][1]]

            tocka3 = lista_tocaka_poligona[lista_poligona[i][2]]


            medo5.add(3, GL_LINE_LOOP, None,
                      ('v2f',
                       ((tocka1[0] + pomak+tocka[brojac_tocki][0]) * povecanje, (tocka1[1] + pomak+tocka[brojac_tocki][1]) * povecanje,
                        (tocka2[0] + pomak+tocka[brojac_tocki][0]) * povecanje, (tocka2[1] + pomak+tocka[brojac_tocki][1]) * povecanje,
                        (tocka3[0] + pomak+tocka[brojac_tocki][0]) * povecanje, (tocka3[1] +tocka[brojac_tocki][1]+ pomak) * povecanje)),
                      ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0)))


            medo5.add(3, GL_LINE_LOOP, None,
                      ('v3f',
                       ((tocka1[0] + pomak + tocka[brojac_tocki][0]) * povecanje,
                        (tocka1[1] + pomak + tocka[brojac_tocki][1]) * povecanje,
                        (tocka1[2] + pomak + tocka[brojac_tocki][2]) * povecanje,
                        (tocka2[0] + pomak + tocka[brojac_tocki][0]) * povecanje,
                        (tocka2[1] + pomak + tocka[brojac_tocki][1]) * povecanje,
                        (tocka2[2] + pomak + tocka[brojac_tocki][2]) * povecanje,
                        (tocka3[0] + pomak + tocka[brojac_tocki][0]) * povecanje,
                        (tocka3[1] + tocka[brojac_tocki][1] + pomak) * povecanje,
                        (tocka3[2] + pomak + tocka[brojac_tocki][2]) * povecanje)),
                      ('c3B', (255, 0, 255, 255, 0, 255, 255, 0, 0)))


Crtaj(1)

def izracunaj_razliku(ri,ti):
    T = [2*ti,1]
    B = 1 / 2 * np.array([[-1, 3, -3, 1],
                          [2, -4, 2, 0]])
    kopija_liste = lista_putanje
    R = np.array([kopija_liste[ri-1],kopija_liste[ri],
                  kopija_liste[ri+1],kopija_liste[ri+2]])
    TB = np.dot(T,B)
    TBR = np.dot(TB,R)

    return TBR


def DCM(brojac_tocki):
    tocka_za_rot = np.array([tocka[brojac_tocki][0],tocka[brojac_tocki][1],tocka[brojac_tocki][2]])
    tangent_za_rot = np.array([tangenta[brojac_tocki][0],tangenta[brojac_tocki][1],tangenta[brojac_tocki][2]])
    za_ri = int(brojac_tocki/(len(lista_putanje)-2)+1)
    ti = int(brojac_tocki%(len(lista_putanje)-2))
    ti /= 20
    deriv = izracunaj_razliku(za_ri,ti)

    rotacija = np.cross(tocka_za_rot,tangent_za_rot)

    sljedeca = np.dot(tocka_za_rot,tangent_za_rot)
    rot_norm = np.linalg.norm(tocka_za_rot)
    sljed_norm = np.linalg.norm(tangent_za_rot)
    kut = (np.arccos(sljedeca/(rot_norm*sljed_norm)))
    U = np.cross(tangent_za_rot,[deriv[0],deriv[1],deriv[2]])
    V = np.cross(tangent_za_rot,U)
    Rmatrix = np.array([tangent_za_rot,U,V.transpose()])
    print(Rmatrix)
    glRotatef(kut,0,0,rotacija[2])



@window.event
def on_draw():
    window.clear()
    #medo2.draw()
    medo.draw()
    medo3.draw()
    DCM(brojac_tocki)
    medo5.draw()
    '''
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75,1,0.05,1000)
    gluLookAt(100,100,100,0,0,0,0,1.0,0)

    '''




@window.event
def on_mouse_press(x,y,button,modifiers):
    global brojac_tocki
    Crtaj(brojac_tocki)
    brojac_tocki+=1




glFrontFace(GL_CCW)
pyglet.app.run()
