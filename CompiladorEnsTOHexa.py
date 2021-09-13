from Traductor import Traductor
from Archivador import GestionadorArchivos

"""
Programa compilador de codigo ensamblador a codigo hexadecimal.
Programa creado para generar los codigos hexadecimales que se guardaran en una memoria
ROM que sera usada para probar microprocesadores propios.
"""

print(f'Andrés Rivera Márquez.')
print(f'''Este programa realiza la conversión de un archivo de texto de código
ensamblador a un archivo de texto que contiene su representación en código
hexadecimal para su guardado en una memoria ROM.''')

RutaEnsamblador = 'Ensamblador.txt'
RutaHexadecimal = 'Hexadecimal.txt'
if __name__ == '__main__':
    try:
        d = None
        while d != 0:
            print(f'''
Que desea realizar?
1: Traducir codigo a Hexadecimal
0: Finalizar''')
            d = int(input('Ingrese la opcion deseada: '))
            print('\n')
            if d == 1:
                Compilador = GestionadorArchivos(RutaEnsamblador, RutaHexadecimal)

                Compilador.crear_archivos()
                CodEnsa = Compilador.leer_archivo()

                if CodEnsa == 0:
                    print(f'El archivo {RutaEnsamblador} no contiene información...')
                else:
                    print(f'Se obtuvo la información de {RutaEnsamblador}...')
                    CodHexa = Traductor.traducir(CodEnsa)
                    if CodHexa == -1:
                        print('No se ha podido realizar la conversión...')
                    else:
                        Compilador.escribirarchivo(CodHexa)
                        print(f'Se ha generado el archivo {RutaHexadecimal} exitosamente...')
    except Exception as e:
        print(f'Hubo un error {e}')
