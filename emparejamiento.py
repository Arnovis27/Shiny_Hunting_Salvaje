import cv2
import numpy as np

def metodo_emparejamiento(imagen_escena, sprite, umbral):
    # Convertir imágenes a escala de grises
    imagen_escena_gris = cv2.cvtColor(imagen_escena, cv2.COLOR_BGR2GRAY)
    sprite_gris = cv2.cvtColor(sprite, cv2.COLOR_BGR2GRAY)

    # Realizar la coincidencia de plantillas
    resultado_correlacion = cv2.matchTemplate(imagen_escena_gris, sprite_gris, cv2.TM_CCOEFF_NORMED)

    # Encontrar las ubicaciones donde la coincidencia es superior al umbral
    loc = np.where(resultado_correlacion >= umbral)

    # Dibujar rectángulos alrededor de las coincidencias encontradas
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imagen_escena, pt, (pt[0] + sprite.shape[1], pt[1] + sprite.shape[0]), (0, 255, 0), 2)

    # Si hay al menos una coincidencia, el sprite está presente
    sprite_presente = len(loc[0]) > 0

    return sprite_presente