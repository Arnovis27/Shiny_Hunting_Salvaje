from emulador import ventana
from acciones import buscar_pokemon, huir, presionar_b
from screenshot import captura_pantalla
from emparejamiento import metodo_emparejamiento
import time, cv2

def main():
    umbral= 0.99
    combate= cv2.imread("C:/Users/arnov/Documents/Python/Shiny_Salvaje/Ruta/combate.PNG")
    valor, dimension= ventana()

    if valor == True:
        contador_encuentros=0

        while True:
            aux=0 #se vuelve 1 si al menos el pokemon fue identificado una vez dentro la busqueda
            buscar_pokemon()
            time.sleep(1) #Segundos de aparicion del pokemon salvaje 
            presionar_b()
            time.sleep(1)
            captura_pantalla(dimension)
            entorno= cv2.imread("C:/Users/arnov/Documents/Python/Shiny_Salvaje/Captura/captura_escene.png")
            
            #se verifica si entro en combate o no
            combate_presente= metodo_emparejamiento(entorno, combate, umbral)
            if combate_presente:
                for i in range(4): #Ajustar al numero de pokemon que aparece  por rutas
                    sprite= cv2.imread("C:/Users/arnov/Documents/Python/Shiny_Salvaje/Ruta/Desierto/{}.PNG".format(i+1))
                    pokemon_presente= metodo_emparejamiento(entorno, sprite, umbral)
                    if pokemon_presente:
                        huir()
                        aux= 1

                if aux==0:
                    break #rompe el ciclo, while, porque ha encontrado shiny?

                contador_encuentros+=1 #Pone ciclo para saber cuantos pokemon ha visto.
                print("Pokemon salvaje #{}".format(contador_encuentros))

    else:
        print("Emulador Cerrado")
                

if __name__ == '__main__':
    main()