import time
import pygetwindow as gw

def ventana():
    # Título de la ventana que estamos buscando
    titulo_ventana = 'VisualBoyAdvance'

    # Obtener todas las ventanas con el título proporcionado
    ventanas = gw.getWindowsWithTitle(titulo_ventana)

    if ventanas:
        # Puedes activar la ventana si lo necesitas
        emulador_window = ventanas[0]
        emulador_window.activate()
        return True
    else:
        return False