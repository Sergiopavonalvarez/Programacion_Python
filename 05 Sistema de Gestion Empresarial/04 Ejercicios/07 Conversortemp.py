



temperatura = float(input("Ingresa la temperatura: "))
unidad = input("Ingresa la unidad (C o F): ")


if unidad.upper() == 'C':
    celsius = (temperatura - 32) * 5/9
    print(f"La temperatura equivalente en Celsius es: {celsius:.2f}°C")
elif unidad.upper() == 'F':
    fahrenheit = temperatura * 9/5 + 32
    print(f"La temperatura equivalente en Fahrenheit es: {fahrenheit:.2f}°F")
else:
    print("Unidad no válida. Ingresa 'C' para Celsius o 'F' para Fahrenheit.")
