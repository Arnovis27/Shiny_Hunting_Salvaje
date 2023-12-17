from emulador import ventana
from acciones import buscar_pokemon, huir, presionar_b
from screenshot import captura_pantalla
import time

def main():
    valor, dimension= ventana()
    if valor == True:
        buscar_pokemon()
        time.sleep(1) #Segundos de aparicion del pokemon salvaje 
        presionar_b()
        time.sleep(1)
        captura_pantalla(dimension)

  

if __name__ == '__main__':
    main()