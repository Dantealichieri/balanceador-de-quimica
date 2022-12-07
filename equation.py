from random import randint
from math import gcd
from functools import reduce


class Equação:

    def __init__(self, equation):

        self.left = list()
        self.right = list()
        self.balanced = True

        integrantes = '0123456789'
        split = equation.split(' = ')
        left = split[0]
        right = split[1]
        left_componentes = left.split(' + ')
        right_componentes = right.split(' + ')
        total_esquerda = dict()
        total_right = dict()

        for component in left_componentes:
            left_counts = dict()
            for ind in range(0, len(component)):
                if component[ind] == ')':
                    if component[ind - 2] == '(':
                        elemento = component[ind - 1]
                    elif component[ind - 3] == '(':
                        elemento = component[ind - 2:ind]
                    try:
                        if component[ind + 3] in integrantes:
                            number = int(component[ind + 1:ind + 4])
                        elif component[ind + 2] in integrantes:
                            number = int(component[ind + 1:ind + 3])
                        else:
                            number = int(component[ind + 1])
                    except IndexError:
                        try:
                            if component[ind + 2] in integrantes:
                                number = int(component[ind + 1:ind + 3])
                            else:
                                number = int(component[ind + 1])
                        except IndexError:
                            number = int(component[ind + 1])
                    if elemento in left_counts:
                        left_counts[elemento] += number
                    else:
                        left_counts[elemento] = number
                    if elemento in total_esquerda:
                        total_esquerda[elemento] += number
                    else:
                        total_esquerda[elemento] = number
            self.left.append(left_counts)

        for component in right_componentes:
            right_contador = dict()
            for ind in range(0, len(component)):
                if component[ind] == ')':
                    if component[ind - 2] == '(':
                        elemento = component[ind - 1]
                    elif component[ind - 3] == '(':
                        elemento = component[ind - 2:ind]
                    try:
                        if component[ind + 3] in integrantes:
                            number = int(component[ind + 1:ind + 4])
                        elif component[ind + 2] in integrantes:
                            number = int(component[ind + 1:ind + 3])
                        else:
                            number = int(component[ind + 1])
                    except IndexError:
                        try:
                            if component[ind + 2] in integrantes:
                                number = int(component[ind + 1:ind + 3])
                            else:
                                number = int(component[ind + 1])
                        except IndexError:
                            number = int(component[ind + 1])
                    if elemento in right_contador:
                        right_contador[elemento] += number
                    else:
                        right_contador[elemento] = number
                    if elemento in total_right:
                        total_right[elemento] += number
                    else:
                        total_right[elemento] = number
            self.right.append(right_contador)

        for key in total_esquerda:
            if total_esquerda[key] != total_right[key]:
                self.balanced = False
            else:
                continue

    def balance(self):

        if self.balanced:
            string = str()
            for dictionary in self.left:
                componente = str()
                for key in dictionary:
                    componente += key
                    componente += str(dictionary[key])
                string += componente
                string += ' + '
            string = string[:len(string) - 3] + ' = '
            for dictionary in self.right:
                componente = str()
                for key in dictionary:
                    componente += key
                    componente += str(dictionary[key])
                string += componente
                string += ' + '
            string = string[:len(string) - 2]
            return string
        else:
            while not self.balanced:
                temp_left = list()
                temp_right = list()
                total_left = dict()
                total_direita = dict()

                for item in self.left:
                    new_dict = dict()
                    for key in item:
                        new_dict[key] = item[key]
                    temp_left.append(new_dict)

                for item in self.right:
                    new_dict = dict()
                    for key in item:
                        new_dict[key] = item[key]
                    temp_right.append(new_dict)

                coeficientes_esq = [randint(1, 10) for _ in range(len(temp_left))]
                coeficientes_dir = [randint(1, 10) for _ in range(len(temp_right))]

                for index in range(0, len(coeficientes_esq)):
                    for key in temp_left[index]:
                        temp_left[index][key] *= coeficientes_esq[index]
                        if key not in total_left:
                            total_left[key] = temp_left[index][key]
                        else:
                            total_left[key] += temp_left[index][key]

                for index in range(0, len(coeficientes_dir)):
                    for key in temp_right[index]:
                        temp_right[index][key] *= coeficientes_dir[index]
                        if key not in total_direita:
                            total_direita[key] = temp_right[index][key]
                        else:
                            total_direita[key] += temp_right[index][key]

                self.balanced = True
                for key in total_left:
                    if total_left[key] != total_direita[key]:
                        self.balanced = False
                    else:
                        continue

            big_tup = tuple(coeficientes_esq + coeficientes_dir)
            coeficientes_esq = list(map(lambda x: int(x / reduce(gcd, big_tup)), coeficientes_esq))
            coeficientes_dir = list(map(lambda x: int(x / reduce(gcd, big_tup)), coeficientes_dir))

            string = str()
            for index in range(0, len(self.left)):
                if coeficientes_esq[index] != 1:
                    componente = str(coeficientes_esq[index])
                else:
                    componente = str()
                for key in self.left[index]:
                    componente += key
                    if self.left[index][key] != 1:
                        componente += str(self.left[index][key])
                    else:
                        continue
                string += componente
                string += ' + '
            string = string[:len(string) - 3] + ' = '
            for index in range(0, len(self.right)):
                if coeficientes_dir[index] != 1:
                    componente = str(coeficientes_dir[index])
                else:
                    componente = str()
                for key in self.right[index]:
                    componente += key
                    if self.right[index][key] != 1:
                        componente += str(self.right[index][key])
                    else:
                        continue
                string += componente
                string += ' + '
            string = string[:len(string) - 2]
            return string