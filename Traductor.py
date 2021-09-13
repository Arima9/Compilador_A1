import os


class Traductor:

    @staticmethod
    def traducir(ensamblador: list):
        """
        :param ensamblador: Este parametro es el codigo rudo en ensamblador del programa
        del procesador que se va a convertir.
        :return: El metodo devuelve una lista con los codigos en hexadecimal deñ programa
        """

        # Lista de Mnemonicos para comparar en las instrucciones
        Mnemonics = ['MOV', 'ADD', 'AND', 'OR', 'NOT', 'XOR', 'LSL', 'LSR', 'JMP', 'JC', 'JZ', 'JSR']

        # Variables necesarias y listas
        ensamble = []  # Aqui se guardara el codigo hexadecimal traducido
        cntprg = 0  # Esta variable se encarga de llevar el conteo de la direccion de memoria que se esta traduciendo
        # Diccionario de etiquetas, formato--> "Etiqueta" : "Direccion"
        labels = {}

        # Iterador for de las lineas del archivo ensamblador
        for Linea in ensamblador:
            word = ''  # Cadena temporal donde se guardaran los caracteres alfanumericos par su procesado
            cadena = ''  # Variable temporal donde se colocan los codigos hexadecimales traducidos
            instr = ''  # Cadena temporal donde se colocaran las instrucciones formateadas correctamente

            """
            Se realiza el preprocesamiento del codigo por linea para adaptarlo al siguiente paso.
            Iterador de los caracteres de la linea en analisis
            """
            for char in Linea:

                if char.isalnum():
                    word += char

                elif char == '\n':
                    break

                elif char == ']' or char == '[':
                    if len(word) == 0:
                        instr += char
                    else:
                        instr += word + char
                    word = ''

                # Se identifican los espacios en las lineas de codigo
                elif char == ' ':
                    if word == 'A' or len(word) == 0 or word == 'SP':
                        continue

                    word.upper()
                    if word == 'RTS':
                        continue

                    for M in Mnemonics:
                        if word == M:
                            instr += word + ' '
                            word = ''

                        else:
                            print(f'No se reconoce el caracter')

                elif char == ',':
                    if word == 'A' or word == 'SP':
                        instr += word + ', '
                        word = ''

                # Se añade la capacidad de reconocer Etiquedas para saltos
                elif char == ':':
                    labels.setdefault(word, cntprg)
                    word = ''

                elif char == ';':
                    instr += word + ';\n'

            # Aqui se comienza a decodificar el codigo ensamblador obtenido anteriormente
            if 'MOV A, [' in instr:
                cadena += '01 '
                try:
                    int(instr[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[11:] == '];\n':
                        cadena += f'0{instr[8]} {instr[9:11]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'MOV A, ' in instr:
                cadena += '00 '
                try:
                    int(instr[7:9], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 0)
                    return -1
                else:
                    if instr[9:] == ';\n':
                        cadena += f'{instr[7:9]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 2

            elif 'MOV SP, ' in instr:
                cadena += '09 '
                try:
                    int(instr[8:10], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 0)
                    return -1
                else:
                    if instr[10:] == ';\n':
                        cadena += f'{instr[8:10]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 2

            elif 'MOV [' in instr:
                cadena += '0A '
                try:
                    int(instr[5:8], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[8:] == '], A;\n':
                        cadena += f'0{instr[5]} {instr[6:8]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'JMP ' in instr:
                cadena += '0B '
                try:
                    int(instr[4:7], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[7:] == ';\n':
                        cadena += f'0{instr[4]} {instr[5:7]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'JSR ' in instr:
                cadena += '0E '
                try:
                    int(instr[4:7], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[7:] == ';\n':
                        cadena += f'0{instr[4]} {instr[5:7]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'JC ' in instr:
                cadena += '0C '
                try:
                    int(instr[3:6], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[6:] == ';\n':
                        cadena += f'0{instr[3]} {instr[4:6]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'JZ ' in instr:
                cadena += '0D '
                try:
                    int(instr[3:6], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[6:] == ';\n':
                        cadena += f'0{instr[3]} {instr[4:6]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'ADD A, [' in instr:
                cadena += '02 '
                try:
                    int(instr[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[11:] == '];\n':
                        cadena += f'0{instr[8]} {instr[9:11]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'AND A, [' in instr:
                cadena += '03 '
                try:
                    int(instr[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[11:] == '];\n':
                        cadena += f'0{instr[8]} {instr[9:11]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'LSL A;\n' in instr:
                cadena += '07\n'
                cntprg += 1

            elif 'LSR A;\n' in instr:
                cadena += '08\n'
                cntprg += 1

            elif 'XOR A, [' in instr:
                cadena += '06 '
                try:
                    int(instr[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 1)
                    return -1
                else:
                    if instr[11:] == '];\n':
                        cadena += f'0{instr[8]} {instr[9:11]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 3

            elif 'NOT A;\n' in instr:
                cadena += '05\n'
                cntprg += 1

            elif 'OR A, ' in instr:
                cadena += '04 '
                try:
                    int(instr[6:8], base=16)
                except ValueError:
                    Traductor.desp_errores(instr, len(ensamble), 0)
                    return -1
                else:
                    if instr[8:] == ';\n':
                        cadena += f'{instr[6:8]}\n'
                    else:
                        Traductor.desp_errores(instr, len(ensamble), 3)
                        return -1
                cntprg += 2

            elif 'RTS;\n' in instr:
                cadena += '0F\n'
                cntprg += 1

            else:
                Traductor.desp_errores(instr, len(ensamble), 2)
                return -1

            ensamble.append(cadena)

        return ensamble

    @staticmethod
    def desp_errores(line: str, nline, err):
        """
        Metodo que se encarga de desplegar el texto de los errores del programa
        :param line: Cadena del codigo.
        :param nline: Indice de la linea de codigo.
        :param err: Codigo interno de error
            0 => Error operando tipo N
            1 => Error operando tipo DIR
            2 => Error comando no reconocido
            3 => Linea de codigo con terminacion invalida
        :return:
        """
        nline += 1
        line = line.replace('\n', ' ')

        if err == 0:
            print(f'Error en la linea de código: {nline}...')
            print(f'El operando N en {line}no pertenece a un hexadecimal...')
        elif err == 1:
            print(f'Error en la linea de código: {nline}...')
            print(f'El operando DIR en {line}no pertenece a un hexadecimal...')
        elif err == 2:
            print(f'Error en la linea: {nline}')
            print(f'{line}no es un comando válido...')
        elif err == 3:
            print(f'La linea de codigo {nline}:{line}no terminó como se esperaba...')


if __name__ == '__main__':
    arr = []
    hexa = []
    Ensamble = 'Ensamblador.txt'
    Hexadecimal = 'Chexa.txt'

    if not os.path.exists(Ensamble):
        f = open(Ensamble, 'x')
        f.close()

    try:
        f = open(Ensamble, 'r')
        arr = f.readlines()
    finally:
        f.close()

    hexa = Traductor.traducir(arr)
    if hexa != -1:
        print('Codigo ensamblador'.center(50, '-'))
        for i in arr:
            print(i, end='')

        print('Codigo Hexadecimal'.center(50, '-'))
        for i in hexa:
            print(i, end='')
