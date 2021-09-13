import os


class Traductor:

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

    @staticmethod
    def traducir(ensamblador: list):
        """

        :param ensamblador:
        :return:
        """
        ensamble = []

        for line in ensamblador:
            cadena = ''

            if 'MOV A, [' in line:
                cadena += '01 '
                try:
                    int(line[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[11:] == '];\n':
                        cadena += f'0{line[8]} {line[9:11]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'MOV A, ' in line:
                cadena += '00 '
                try:
                    int(line[7:9], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 0)
                    return -1
                else:
                    if line[9:] == ';\n':
                        cadena += f'{line[7:9]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1


            elif 'MOV SP, ' in line:
                cadena += '09 '
                try:
                    int(line[8:10], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 0)
                    return -1
                else:
                    if line[10:] == ';\n':
                        cadena += f'{line[8:10]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'MOV [' in line:
                cadena += '0A '
                try:
                    int(line[5:8], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[8:] == '], A;\n':
                        cadena += f'0{line[5]} {line[6:8]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'JMP ' in line:
                cadena += '0B '
                try:
                    int(line[4:7], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[7:] == ';\n':
                        cadena += f'0{line[4]} {line[5:7]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'JSR ' in line:
                cadena += '0E '
                try:
                    int(line[4:7], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[7:] == ';\n':
                        cadena += f'0{line[4]} {line[5:7]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'JC ' in line:
                cadena += '0C '
                try:
                    int(line[3:6], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[6:] == ';\n':
                        cadena += f'0{line[3]} {line[4:6]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'JZ ' in line:
                cadena += '0D '
                try:
                    int(line[3:6], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[6:] == ';\n':
                        cadena += f'0{line[3]} {line[4:6]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'ADD A, [' in line:
                cadena += '02 '
                try:
                    int(line[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[11:] == '];\n':
                        cadena += f'0{line[8]} {line[9:11]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'AND A, [' in line:
                cadena += '03 '
                try:
                    int(line[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[11:] == '];\n':
                        cadena += f'0{line[8]} {line[9:11]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'LSL A;\n' in line:
                cadena += '07\n'

            elif 'LSR A;\n' in line:
                cadena += '08\n'

            elif 'XOR A, [' in line:
                cadena += '06 '
                try:
                    int(line[8:11], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 1)
                    return -1
                else:
                    if line[11:] == '];\n':
                        cadena += f'0{line[8]} {line[9:11]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'NOT A;\n' in line:
                cadena += '05\n'

            elif 'OR A, ' in line:
                cadena += '04 '
                try:
                    int(line[6:8], base=16)
                except ValueError:
                    Traductor.desp_errores(line, len(ensamble), 0)
                    return -1
                else:
                    if line[8:] == ';\n':
                        cadena += f'{line[6:8]}\n'
                    else:
                        Traductor.desp_errores(line, len(ensamble), 3)
                        return -1

            elif 'RTS;\n' in line:
                cadena += '0F\n'

            else:
                Traductor.desp_errordes(line, len(ensamble), 2)
                return -1

            ensamble.append(cadena)

        return ensamble

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

