from data_sync import SincronizadorDatos

sincronizador = SincronizadorDatos()

# Sincronizar con NASA Horizons
sincronizador.sincronizar_posiciones_planetarias()

# Sincronizar con datos solares
sincronizador.sincronizar_datos_solares()
