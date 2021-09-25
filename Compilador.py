from Traductor import Traductor
from Archivador import GestionadorArchivos

"""
Autor: Andres Rivera Marquez
Ingeniero en Mecatronica por el Instituto Tecnologico de Sonora.

Descripcion: Debido a la necesidad de programar en codigo hexadecimal para
realizar programas de testing en mi proyecto de tesis, decidí iniciar este 
pequenio proyecto, el cual es un compilador para el codigo ensamblador, 
utilizando los mnemonicos con la lista de parametros listados en la hoja de
datos del procesador de mi tesis.

Version:
Segunda version del programa Compilador_A1, creado a partir de la primera
version estable y funcional. En esta version se desea agregar flexibilidad
a la hora de programar en ensamblador, permitiendo variaciones en los espacios
varios usos de tipos de numeros, y varias mejoras mas.

FUNCIONALIDADES POR ANIADIR:
----Flexibilidad en el uso de espacios para codificar.
----Capacidad de utilizar variables.
----Capacidad de utilizar etiquetas para saltos.
    *Se necesitara llevar un control de la posicion de la memoria
    *Se debe tomar en cuenta cada instruccion analizada.
    *Analizar etiquetas inexistentes
    *
----Generacion del archivo hexadecimal en formato Intelhex
    *Capacidad de seleccionar el tipo de archivo
        #8 Bits IntelHex
        #16 Bits IntelHex
        #32 Bits IntelHex

FUNCIONALIDADES ANIADIDAS:
----Capacidad de ingresar un nombre de archivo propio y crear un archivo
    nuevo utilizando el mismo nombre.

"""



if __name__ == '__main__':
    
    #Se crean las variables tipo string que alojaran el nombre del archivo
    #que se desea convertir, y donde se alojara el codigo hexadecimal.
    RutaEnsamblador = ''
    RutaHexadecimal = ''
    
    #Se crea una variable bool para generar un ciclo infinito
    d = True

    #Bloque try_catch para manejar errores en el codigo sin salir abruptamente
    try:

        #Se inicia el ciclo en el cual se ejecutara el programa.
        while d:

            #Se le pide al usuario que ingrese el nombre del archivo de codigo
            #fuente que desea compilar.
            RutaEnsamblador = input('Nombre completo del archivo a convertir: ')
            
            #Se crea el nombre del archivo nuevo donde se colocara
            #posteriormente el codigo en hexadecimal.
            RutaHexadecimal = "Nuevo_" + RutaEnsamblador
            print('\n')

            #Se instancia un objeto llamado compilador a partir de la clase
            #GestionadorArchivos dandole como parametros los nombres de los
            #archivos fuente y compilado.
            Compilador = GestionadorArchivos(RutaEnsamblador, RutaHexadecimal)
            
            #Se llama al metodo crear_archivo del objeto Compilador, este
            #creara el archivo nuevo donde se guardara el codigo compilado
            Compilador.crear_archivo()

            #Se llama al metodo leer_archivo y se guarda el retorno en una
            #variable, dicho return es una lista de strings con el codigo
            #fuente.
            CodEnsa = Compilador.leer_archivo()

            #Si el metodo leer_archivo regresa un 0, se despliega un mensaje de
            #error.
            if CodEnsa == 0:
                print(f'El archivo {RutaEnsamblador} no contiene información...')
            
            #En caso de no haber error entonces se realiza la conversion
            else:
                #Se llama al metodo traducir de Traductor, se le da una lista
                #con el codigo fuente a traducir, y el retorno se guarda en
                #CodHexa
                CodHexa = Traductor.traducir(CodEnsa)
                
                #En caso de que haber retornado un codigo -1 se despliega un
                #mensaje de error.
                """
                Agregar distintos tipos de errores al if
                """
                if CodHexa == -1:
                    print('No se ha podido realizar la conversión...')
                
                #En caso de no haber error, se escribe el codigo hexadecimal
                #en el archivo nuevo creado recien
                else:
                    Compilador.escribirarchivo(CodHexa)
                    print("Se ha generado el archivo {RutaHexadecimal} 
                            exitosamente...")
    except Exception as e:
        print(f'Hubo un error {e}')
