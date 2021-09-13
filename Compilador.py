from Traductor import Traductor
from Archivador import GestionadorArchivos

"""
Segunda version del programa compilador de codigo ensamblador a hexadecimal.

MEJORAS:
N/A

Andrés Rivera Márquez.
Ingeniero en Mecatrónica.
ITSON.
"""


RutaEnsamblador = ''
RutaHexadecimal = ''
d = True
if __name__ == '__main__':
    try:
        while d:
            RutaEnsamblador = input('Nombre del archivo a convertir: ')
            RutaHexadecimal = "Nuevo_" + RutaEnsamblador
            print('\n')

            Compilador = GestionadorArchivos(RutaEnsamblador, RutaHexadecimal)
            Compilador.crear_archivo()
            CodEnsa = Compilador.leer_archivo()

            if CodEnsa == 0:
                print(f'El archivo {RutaEnsamblador} no contiene información...')
            else:
                CodHexa = Traductor.traducir(CodEnsa)
                if CodHexa == -1:
                    print('No se ha podido realizar la conversión...')
                else:
                    Compilador.escribirarchivo(CodHexa)
                    print(f'Se ha generado el archivo {RutaHexadecimal} exitosamente...')
    except Exception as e:
        print(f'Hubo un error {e}')
