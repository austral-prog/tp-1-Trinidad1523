def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horas = total_segundos // 3600
    print(horas)
    resto_horas = total_segundos % 3600
    minutos = resto_horas // 60
    print(minutos)
    resto_minutos = resto_horas % 60
    print (resto_minutos)

#time()
