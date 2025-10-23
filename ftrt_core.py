from ftrt_core import FTRTCalculator

# Inicializar calculadora
calculadora = FTRTCalculator()

# Calcular FTRT para fecha específica
resultado = calculadora.calcular_ftrt_total("2024-05-10")
print(f"FTRT: {resultado['ftrt_normalizada']:.2f}")

# Generar alerta
alerta = calculadora.generar_alerta("2024-05-10")
print(f"Nivel: {alerta['nivel_riesgo']}")
