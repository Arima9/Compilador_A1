import os

class GestionadorArchivos:

    def __init__(self, rutaensa, rutahexa):
        self._rutaEnsa = rutaensa
        self._rutaHexa = rutahexa
        self.contadorbytes = 0

    @property
    def rutaEnsa(self):
        return self._rutaEnsa

    @property
    def rutaHexa(self):
        return self._rutaHexa

    @rutaEnsa.setter
    def rutaEnsa(self, rutaEnsa):
        self._rutaEnsa = rutaEnsa

    @rutaHexa.setter
    def rutaHexa(self, rutaHexa):
        self._rutaHexa = rutaHexa

    def crear_archivo(self):
        """Este metodo se encarga de crear los archivos necesarios
        en formato txt, el primero donde se colocará el código ensamblador
        y el segundo donde se colocará la traducción al código hexadecimal"""

        if os.path.exists(self._rutaEnsa):
            print(f'Archivo {self._rutaEnsa} encontrado...')

            if os.path.exists(self._rutaHexa):
                print(f'Archivo {self._rutaHexa} encontrado...')
            else:
                f = open(self._rutaHexa, 'x', encoding='utf8')
                f.close()
                print(f'Archivo {self._rutaHexa} generado...')
        else:
            print(f'Archivo {self._rutaEnsa} no existe...')



    def leer_archivo(self):
        lista = []
        f = open(self._rutaEnsa, 'r', encoding='utf8')
        lista = f.readlines()
        f.close()
        if len(lista) == 0:
            return 0
        return lista

    def escribirarchivo(self, ensamble:list):
        f = open(self._rutaHexa, 'w', encoding='utf8')
        f.write(f'Inicio del ensamble'.center(50, '-'))
        f.write('\n')
        for line in ensamble:
            f.write(line)
        f.write(f'Fin del ensamble'.center(50, '-'))
        f.write('\n')
        f.close()

if __name__ == '__main__':
    Compil = GestionadorArchivos('Prueba1.txt', 'Prueba2.txt')
    Compil.crear_archivos()
    lista = Compil.leer_archivo()
    if lista == 0:
        print(f'El archivo esta vacio..')
    else:
        Compil.escribirarchivo(lista)