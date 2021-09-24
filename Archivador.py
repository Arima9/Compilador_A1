"""
Esta es la clase de GestionadorArchivos, esta clase tiene metodos
relacionados con el manejo de los archivos de codigo con los que se 
estara trabajando. Creacion, obtencion de informacion y escritura a estos
archivo.
"""

#Se importa la biblioteca os para majear el sistema operativo actual.
import os

#Se declara la clase
class GestionadorArchivos:
    
    #Sobrecarga del metodo constructor __init__
    """
    Se le daran como parametros, self, la ruta del codigo ensamblador
    y la ruta del codigo hexadecimal. En este caso al ser unicamente los
    nombres, estara trabajando con archivos que estaran ubicados en el mismo
    directorio que el programa principal
    """
    def __init__(self, rutaensa, rutahexa):
        self._rutaEnsa = rutaensa
        self._rutaHexa = rutahexa
        self.contadorbytes = 0

    #Definicion de los setter y los getter de la clase.
    
    #Getters
    @property
    def rutaEnsa(self):
        return self._rutaEnsa
    @property
    def rutaHexa(self):
        return self._rutaHexa

    #Setters
    @rutaEnsa.setter
    def rutaEnsa(self, rutaEnsa):
        self._rutaEnsa = rutaEnsa

    @rutaHexa.setter
    def rutaHexa(self, rutaHexa):
        self._rutaHexa = rutaHexa

    #Definicion del metodo que se encarga de crear el archivo
    def crear_archivo(self):
    """
    Añadir decicion para crear archivo en caso de no existir, o la capacidad
    de ingresar de nuevo el nombre del archivo para su correcion.
    """

        #Si el nombre del archivo existe en el directorio desplega el mensaje
        if os.path.exists(self._rutaEnsa):
            print(f'Archivo {self._rutaEnsa} encontrado...')
            
            #Si ya existe un archivo hexadecimal, se informa.
            if os.path.exists(self._rutaHexa):
                print(f'Archivo {self._rutaHexa} encontrado...')
            
            #En caso de no existir se crea un archivo exadecimal nuevo
            else:
                f = open(self._rutaHexa, 'x', encoding='utf8')
                f.close()
                print(f'Archivo {self._rutaHexa} generado...')

        #En caso de no existir el archivo con el codigo fuente, se despliega un
        #mensaje indicando su inexistencia
        else:
            print(f'Archivo {self._rutaEnsa} no existe...')


    #Se define el metodo para leer el archivo de codigo fuente.
    def leer_archivo(self):
        #Creacion de una lista para guardar los datos del archivo.
        lista = []

        #Se anre el archivo codigo fuente en modo de lectura con unicode
        f = open(self._rutaEnsa, 'r', encoding='utf8')

        #Se guardan todas las lineas del archivo como strings en la lista 
        lista = f.readlines()

        #Se cierra el archivo para liberar memoria
        f.close()

        #Si el tamaño del archivo es cero, es decir vacio, entonces se devuelve
        #un cero
        if len(lista) == 0:
            return 0
        
        #Si no, se devuelve la lista con las lineas de codigo.
        return lista

    #Definicion del metodo para escribir informacion en el archivo hexadecimal
    def escribirarchivo(self, ensamble:list):

        #Se abre el archivo en escritura con unicode
        f = open(self._rutaHexa, 'w', encoding='utf8')
        
        #Se escribe una linea de encabezado, y al final un salto de linea
        f.write(f'Inicio del ensamble'.center(50, '-'))
        f.write('\n')

        #Se crea un iterador for para, y se asigna cada linea en la lista
        #ensamble a line.
        for line in ensamble:
            #Se escribe cada linea de la lista en el archivo
            f.write(line)

        #Se escribe un final de archivo con su salto de linea
        f.write(f'Fin del ensamble'.center(50, '-'))
        f.write('\n')

        #Se cierra el archivo para liberar la memoria
        f.close()

#Codigo ejecutable al probar el codigo como principal
if __name__ == '__main__':
    Compil = GestionadorArchivos('Prueba1.txt', 'Prueba2.txt')
    Compil.crear_archivos()
    lista = Compil.leer_archivo()
    if lista == 0:
        print(f'El archivo esta vacio..')
    else:
        Compil.escribirarchivo(lista)
