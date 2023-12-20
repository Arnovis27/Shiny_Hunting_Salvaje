# Proyecto Pokémon Shiny Finder

Este proyecto está diseñado para ayudarte a encontrar Pokémon Shiny en el juego Pokémon Esmeralda mediante el reconocimiento de imágenes.

## Características Principales

- **Saltos en Bici Acrobatica:** El algoritmo es capaz de hacer saltos en bici para encontrar pokemon salvajes ya sea en hierba o en ruta.
- **Encuentro Inicial:** Pulsa la tecla `Z` para iniciar el encuentro con el Pokémon salvaje.
- **Análisis de Imágenes:** Utiliza técnicas de reconocimiento de imágenes para analizar si el encuentro es un Pokémon Shiny.
- **Huir:** Es capaz de huir si el pokemon no es shiny y repite el proceso desde los saltos en bici.

## Configuracion del emulador  
Para aumentar la velocidad del emulador y funcione mas rapido la busqueda  
**Options** > **Frame Skip** > **Throttle** > **Other** > **1000**  
Para ejecutar la ventana del emulador, debes hacerlo en
**Options** > **Video** > **x2**  


## Configuracion del juego  
Muy importante que te dirijas a opciones del juego y realices:  
- Velocidad del texto: Rapida  
- Animacion de Combate: No  
Esto con el fin de optimizar el tiempo en los encuentros.  
Este programa NO abre el juego automaticamente, debes establecer al personaje en la zona de caza con una bici acrobatica y un pokemon que tenga de habilidad **Iluminacion** como lider de equipo, es recomendable que el pokemon tenga equipado el objeto **Bola Humo** para que siempre pueda huir del combate y que de nombre solo tenga un caracter, asi se usa menos tiempo para realizar el encuentro.

## Configuración y Uso

1. **Clona el Repositorio:**
   ```bash
   git clone https://github.com/Arnovis27/Shiny_Hunting_Salvaje.git
   cd Shiny_Hunting_Salvaje

2. **Instala Dependencias**
    ```bash
    pip install -r requirements.txt 

3. **Configuracion del sprite**  
    - Asegúrate de proporcionar la ruta correcta del sprite de Pokémon Shiny en ´main.py´. Esto es crucial para el reconocimiento preciso.
    Guiate del que encuetras en la carpeta Ruta en la seccion Desierto, son los archivos.png que esta enumerados por orden numerico.
    - Para poder hacer el shiny hunting, debes proporcionar al codigo una foto de los pokemon que aparecen en la ruta en la que estas buscando el
    pokemon shiny guiate de los que salen en el desierto que se esta usando en este codigo de ejemplo.
    - Es crucial que la imagen de combate.PNG que aparece en la carpeta de Ruta sea exactamente igual siempre, ya que esta determina el estado
    en el que nos encontramos, es decir, con ella podremos saber si estamos dentro de un combate o no para poder pasar al analisis de imagenes de
    los pokemon

4. **Ejecuta el programa**
    ```bash
    python main.py

## Contribuciones  
¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.
