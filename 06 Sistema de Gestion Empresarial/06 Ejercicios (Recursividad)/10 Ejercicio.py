
class OperacionesArray:
    @classmethod
    def imprimir_ascendente(cls, arr, idx=0):
        if idx < len(arr):
            print(arr[idx], end=" ")
            cls.imprimir_ascendente(arr, idx + 1)

    @classmethod
    def imprimir_descendente(cls, arr, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if idx >= 0:
            print(arr[idx], end=" ")
            cls.imprimir_descendente(arr, idx - 1)

    @classmethod
    def suma_elementos(cls, arr, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if idx < 0:
            return 0
        else:
            return arr[idx] + cls.suma_elementos(arr, idx - 1)

    @classmethod
    def contar_ocurrencias(cls, arr, x, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if idx < 0:
            return 0
        else:
            return (arr[idx] == x) + cls.contar_ocurrencias(arr, x, idx - 1)

    @classmethod
    def esta_ordenado_ascendente(cls, arr, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if idx <= 0:
            return True
        else:
            return arr[idx] >= arr[idx - 1] and cls.esta_ordenado_ascendente(arr, idx - 1)

    @classmethod
    def posicion_valor(cls, arr, valor, idx=None):
        if idx is None:
            idx = 0

        if idx < len(arr):
            if arr[idx] == valor:
                return idx
            else:
                return cls.posicion_valor(arr, valor, idx + 1)
        else:
            return -1

    @classmethod
    def duplicar_entre_posiciones(cls, arr, izq, der):
        if izq < der:
            arr[izq] *= 2
            arr[der] *= 2
            cls.duplicar_entre_posiciones(arr, izq + 1, der - 1)

    @classmethod
    def valor_maximo(cls, arr, idx=None):
        if idx is None:
            idx = 0

        if idx == len(arr) - 1:
            return arr[idx]
        else:
            max_resto = cls.valor_maximo(arr, idx + 1)
            return max(arr[idx], max_resto)

    @classmethod
    def posicion_maximo(cls, arr, idx=None):
        if idx is None:
            idx = 0

        if idx == len(arr) - 1:
            return idx
        else:
            max_resto = cls.posicion_maximo(arr, idx + 1)
            return idx if arr[idx] > arr[max_resto] else max_resto

    @classmethod
    def primer_no_nulo(cls, arr, idx=None):
        if idx is None:
            idx = 0

        if idx < len(arr) and arr[idx] != 0:
            return idx
        elif idx == len(arr) - 1:
            return -1
        else:
            return cls.primer_no_nulo(arr, idx + 1)

    @classmethod
    def ceros_consecutivos_al_final(cls, arr, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if idx >= 0 and arr[idx] == 0:
            return 1 + cls.ceros_consecutivos_al_final(arr, idx - 1)
        else:
            return 0

    @classmethod
    def invertir_entre_posiciones(cls, arr, izq, der):
        if izq < der:
            arr[izq], arr[der] = arr[der], arr[izq]
            cls.invertir_entre_posiciones(arr, izq + 1, der - 1)

    @classmethod
    def suma_igual_a_b(cls, arr, b, idx=None):
        if idx is None:
            idx = len(arr) - 1

        if b == 0:
            return True

        if idx < 0:
            return False

        return cls.suma_igual_a_b(arr, b - arr[idx], idx - 1) or cls.suma_igual_a_b(arr, b, idx - 1)

    @classmethod
    def cantidad_menores_que_x(cls, arr, x, idx=None):
        if idx is None:
            idx = 0

        if idx == len(arr):
            return 0
        else:
            return (arr[idx] < x) + cls.cantidad_menores_que_x(arr, x, idx + 1)

    @classmethod
    def impares_posiciones_pares(cls, arr, idx=None):
        if idx is None:
            idx = 0

        if idx == len(arr):
            return 0
        else:
            return (arr[idx] % 2 != 0 and idx % 2 == 0) + cls.impares_posiciones_pares(arr, idx + 1)

    @classmethod
    def primera_subsecuencia_consecutiva(cls, arr, consecutivos=3, idx=None):
        if idx is None:
            idx = 0

        if idx + consecutivos - 1 < len(arr):
            if all(arr[idx + i] == arr[idx + i + 1] - 1 for i in range(consecutivos - 1)):
                return idx
            else:
                return cls.primera_subsecuencia_consecutiva(arr, consecutivos, idx + 1)
        else:
            return -1

# Ejemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("a) Imprimir Ascendente:")
OperacionesArray.imprimir_ascendente(arr)
print("\nb) Imprimir Descendente:")
OperacionesArray.imprimir_descendente(arr)
print("\nc) Suma de todos los elementos:", OperacionesArray.suma_elementos(arr))
x = 3
print(f"d) El valor {x} aparece {OperacionesArray.contar_ocurrencias(arr, x)} veces en el array.")
print("e) ¿El array está ordenado ascendentemente?", OperacionesArray.esta_ordenado_ascendente(arr))
valor_buscar = 7
print(f"f) Posición de {valor_buscar} en el array:", OperacionesArray.posicion_valor(arr, valor_buscar))
izq, der = 2, 7
OperacionesArray.duplicar_entre_posiciones(arr, izq, der)
print("g) Duplicar valores entre posiciones", izq, "y", der, ":", arr)
print("h) Valor máximo del array:", OperacionesArray.valor_maximo(arr))
print("i) Posición del máximo en el array:", OperacionesArray.posicion_maximo(arr))
print("j) Posición del primer elemento no nulo:", OperacionesArray.primer_no_nulo(arr))
print("k) Cantidad de ceros consecutivos al final del array:", OperacionesArray.ceros_consecutivos_al_final(arr))
izq, der = 3, 8
OperacionesArray.invertir_entre_posiciones(arr, izq, der)
print("l) Invertir elementos entre posiciones", izq, "y", der, ":", arr)
b = sum(arr)
print(f"m) ¿{b} es igual a la suma de todos los elementos del array?", OperacionesArray.suma_igual_a_b(arr, b))
x = 6
print(f"n) Cantidad de elementos menores que {x} en el array:", OperacionesArray.cantidad_menores_que_x(arr, x))
print("o) Cantidad de elementos impares en posiciones pares del array:", OperacionesArray.impares_posiciones_pares(arr))
consecutivos = 3
print(f"p) Posición de la primera subsecuencia de {consecutivos} números consecutivos en el array:",
      OperacionesArray.primera_subsecuencia_consecutiva(arr, consecutivos))
