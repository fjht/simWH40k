# -*- coding: utf-8 -*-
from math import sqrt
import random
import re

perfiles = {
    'Marine espacial':  [ 4, 4, 4, 4, 1, 4, 1, 8, '3+'],
    'Sargento marine espacial':  [ 4, 4, 4, 4, 1, 4, 2, 9, '3+'],
    'Sargento Guardia imperial': [ 3, 3, 3, 3, 1, 3, 2, 7, '5+'],
    'Guardia imperial': [ 3, 3, 3, 3, 1, 3, 1, 7, '5+']
}

armas = {           # Alc F  FP Notas
    'Bolter':      ( 24, 4, 5, ['Fuego rapido']),
    'Rifle laser': ( 24, 3, 5, ['Fuego rapido'])
}


def num_disp(notas, dist, is_moving):
    """
    Halla el número de disparos que pueden efectuarse con un arma según la situación
    """

    tipos_arma = {
    'Asalto (\d)':'',
    '(Fuego rapido)':'',
    'Pesada (\d)':''
    }

    for nota in notas:
        for tipo_arma in tipos_arma.keys():
            print re.findall(tipo_arma, nota)
    
def tiradas(fase, tipo_objetivo, notas_arma, *param, **arg):
    """
    Hace las tiradas y devuelve el número de bajas en la unidad objetivo
    """
    if len(param) == 5 and fase == 'CCC':
        atkHA, defHA, F, R, TS = param
    elif len(param) == 4 and fase == 'DISP':
        HP, F, R, TS = param
    elif len(param) == 2 and fase == 'DISP':
        HP, blind = param
    elif len(param) == 3 and fase == 'CCC':
        atkHA, defHA, blindF = param
    # Establecer el número ataques o disparos

    # Tirada para impactar todos los dados calculados

    # Impactos de francotirador: Asignar bajas
    # Repetición de impactos por arma acoplada
    # Armas de precisión

    # Tirada para herir

    # Heridas aceradas
    # Repetición de tiradas para herir (cuchillas relámpago)

    # Tirada de salvación
    # Asignar herida al más cercano y realizar tirada

    # Tiradas de no hay dolor
        

def distancia(*objetos):
    # Falta que vea que si son unidades haga la distancia entre miniatura de la misma unidad
    try:
        (x1, y1) = ( float(a) for a in objetos[0].posicion)
        (x2, y2) = ( float(a) for a in objetos[1].posicion)
        dist = sqrt((x1 - x2 )**2 + (y1 - y2)**2)
        return dist
    except AttributeError:
        print "No esta desplegada alguna de las miniaturas"


def direccion(*objetos):
    """
    Esta función obtiene la dirección entre miniaturas más cercanas de dos unidades
    """
    pass


class miniatura():
    def __init__(self, tipo='infantry', armas='', perfil=''):
        self.tipo = tipo
        self.armas = armas
        self.perfil = perfil
        self.is_moving = False
        self.is_deployed = False
        self.tamano = 1
        self.heridas = self.perfil[4] # Cuando se alcanza 0 se comprueba y si muere se saca del tablero
        #self.transporte

    def desplegar(self, x, y):
        self.posicion = (x, y)

    def distancia(self, objetivo, *alcances):
        (x1, y1) = ( float(a) for a in self.posicion)
        (x2, y2) = ( float(a) for a in objetivo.posicion)
        dist = sqrt((x1 - x2 )**2 + (y1 - y2)**2)
        print "distancia", dist
        print alcances
        try:
            en_alcance = tuple(dist >= float(alcance) for alcance in alcances)
            return dist, en_alcance
        except TypeError:
            pass
        return dist

    def en_distancia(self, objetivo, arma):
        armas[arma]
    
    def mover(self, x, y):
        self.is_moving = True

    def dispara(self, objetivo):
        (alc, F, FP, notas) = self.armas
        R = objetivo.perfil[3]
        TS = objetivo.perfil[-1]
        # comprobar alcance
        dist , (en_alcance) = self.distancia(objetivo, alc)
        print dist, en_alcance
        # determina número de disparos
        num_disp(notas, dist, self.is_moving)

    def destruir():
        pass


comp_escuadras = {
    'Escuadra tactica': ['Sargento Marine'] + 4 * ['Marine espacial'],
    'Escuadra infanteria': ['Sargento Guardia imperial'] + 9 * ['Guardia imperial']
}


class unidad():
    """
    Esta clase es la que engloba a diferentes miniaturas que se han de mover juntas.
    Las unidades pueden tener solo una miniatura.
    Los personajes independientes pueden añadirse a las unidades
    """
    def __init__(self, nombre_unidad, tipo_escuadra):
        self.nombre_unidad = nombre_unidad
        self.composicion = [ miniatura(perfil=perf, armas=armas['Bolter'])
                            for perf in comp_escuadras[tipo_escuadra]]

    def distancia_a(self, objeto):
        return min([distancia(mini, objeto) for mini in self.composicion])

    def disparar_a(self, objetivo):
        pass

    def estimar_objetivo(self):
        """
        Esta función simula las bajas que se pueden causar a las diferentes unidades del enemigo
        en cada turno.
        Así pues determina el movimiento, 
        Mover
        Asaltar(objetivo)
        Correr(direccion) 
        Disparar()

        """
        pass

    def mover_hacia(self, direccion, expandir=True, maximo=True):
        """
        Se puede
        """
        pass

    def estimar_bajas(self, objetivo):
        pass

    def coherencia_escuadra(self):
        """
        Falta hacer que solo compruebe sin repetición
        """
        for m1 in self.composicion:
            for m2 in self.composicion[1:]:
                if distancia(m1, m2) >= 2. + 1.: return False # Hay que añadir el tamaño de la peana
        return True

class juego():
    def __


class ejercito():
    pass

class codex():
    pass

escuadra1 = miniatura(perfil='Marine espacial', armas=armas['Bolter'])
escuadra1.desplegar(3.,5)

escuadra2 = miniatura(tipo='jump', perfil=perfiles['Guardia imperial'])
escuadra2.desplegar(3,25)
escuadra3 = miniatura(perfil=perfiles['Guardia imperial'])
escuadra3.desplegar(2,60)
print escuadra3.posicion

#print "distancia"
#print escuadra1.distancia(escuadra2)

print escuadra1.dispara(escuadra2)
print escuadra1.dispara(escuadra3)

for i in range(3):
    pass
    #print random.randint(1, 6)

print num_disp(['Asalto 4'], 15, True)
print num_disp(['Fuego rapido'],15, False)
print num_disp(['Fuego rapido'],4, True)

tact1 = unidad('Escuadra tactica Lucius', 'Escuadra tactica')
for soldado in tact1.composicion:
    print soldado.perfil
    soldado.desplegar(random.randint(0,3),random.randint(0,2))


print distancia(tact1.composicion[0],tact1.composicion[1])
print tact1.coherencia_escuadra()

print tact1.distancia_a(escuadra2)
print tact1.distancia_a(escuadra1)
print tact1.distancia_a(escuadra3)