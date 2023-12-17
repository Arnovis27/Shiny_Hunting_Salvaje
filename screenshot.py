import pyautogui
import os

def captura_pantalla( emulador_window):
    # Crear la carpeta de comparación en el escritorio
    carpeta_comparacion = 'C:/Users/arnov/Documents/Python/Shiny_Salvaje/Captura'

    # Verificar si la carpeta ya existe, si no, crearla
    if not os.path.exists(carpeta_comparacion):
        os.makedirs(carpeta_comparacion)

    # Obtener la posición y el tamaño de la ventana del emulador
    left, top, width, height = emulador_window.left, emulador_window.top, emulador_window.width, emulador_window.height
    # Captura de pantalla de la ventana del emulador
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot_path = os.path.join(carpeta_comparacion, f'captura_escene.png')
    screenshot.save(screenshot_path)
    print("Estado guardado")