import pyautogui
import time

def buscar_pokemon():
    #saltos en bici acrobatica
    time.sleep(1)
    pyautogui.keyDown('x')
    time.sleep(2)
    pyautogui.keyUp('x')

def presionar_b():
    for _ in range(3):
        pyautogui.keyDown('x')
        pyautogui.keyUp('x')

def huir():
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')
    pyautogui.keyUp('d')
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')
    time.sleep(1)
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')