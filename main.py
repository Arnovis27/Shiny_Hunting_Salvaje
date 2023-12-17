from emulador import ventana
from acciones import buscar_pokemon, huir

def main():
    valor= ventana()
    if valor == True:
        buscar_pokemon()

if __name__ == '__main__':
    main()