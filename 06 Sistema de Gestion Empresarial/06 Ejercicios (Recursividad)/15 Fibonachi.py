
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Definimos la cantidad de números de Fibonacci que queremos generar
n = 10  # Puedes cambiar este valor según la cantidad que desees

# Llamamos a la función fibonacci() y mostramos el resultado
fibonacci_sequence = fibonacci(n)
print("Los primeros", n, "números de Fibonacci son:", fibonacci_sequence)