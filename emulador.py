import pyautogui
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

        # Calcular las coordenadas relativas al centro de la ventana
        center_x, center_y = emulador_window.left + emulador_window.width // 2, emulador_window.top + emulador_window.height // 2

        # Hacer clic en el centro de la ventana
        pyautogui.click(center_x, center_y)
        
        return True, emulador_window
    else:
        return False, None