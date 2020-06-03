#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Daniel Steven Betancourt Correa < BETA >
# Automatizacion de interfaz grafica
# https://automatetheboringstuff.com/chapter18/
# modulo PyAutoGUI’s -> Modulo de mouse y teclado.
# Documentación completa https://pyautogui.readthedocs.io/en/latest/
import pyautogui,time
pyautogui.PAUSE = 0.5           # PAUSE
pyautogui.FAILSAFE = True       # Superiro izquierda - mov mause
#%%----> Resolucion de pantalla
print(pyautogui.size())
# resolucion de pantalla 1366x768
ancho, alto = pyautogui.size()
#   0                   1365  (eje_x)
#   #-------------------# 0 
#   |                   |
#   |                   |
#   |                   |
#   |                   |
#   #-------------------# 765 (eje_y)
#%%
pyautogui.moveTo(1800, 400, duration=0.15)
#%%----> Mover el mouse
print("\nMovimiento de mause\n")
# Obtener posicion del mause
pos_mouse_x, pos_mouse_y = pyautogui.position()
# movimiento en posición de coordenadas de la pantalla
for i in range(3):
    print("Vuelta %d"%i)
    pyautogui.moveTo(400, 400, duration=0.15)
    pyautogui.moveTo(500, 400, duration=0.15)
    pyautogui.moveTo(500, 500, duration=0.15)
    pyautogui.moveTo(400, 500, duration=0.15)
# movimiento en referencia a la ultima posición
for i in range(3):
    print("Vuelta %d"%i)
    pyautogui.moveRel(100, 0,   duration=0.15)
    pyautogui.moveRel(0, 100,   duration=0.15)
    pyautogui.moveRel(-100, 0,  duration=0.15)
    pyautogui.moveRel(0, -100,  duration=0.15)
#%% Proyecto Mouse
#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        # TODO: Get and print the mouse coordinates.
        pos_mouse_x, pos_mouse_y = pyautogui.position()
        print("X= "+str(pos_mouse_x)+"Y= "+str(pos_mouse_y)+"\n")
except KeyboardInterrupt:
    print('\nDone.')
#%%
while True:
# TODO: Get and print the mouse coordinates.
    pos_mouse_x, pos_mouse_y = pyautogui.position()
    print("X= "+str(pos_mouse_x)+"Y= "+str(pos_mouse_y)+"\n") 
#%%----> Mover el mouse
# mouseDown() & mouseUp() -> click
pyautogui.click(1248,17)
pyautogui.rightClick()  # Simula un clic con el botón derecho.
pyautogui.middleClick() # Simula un clic del botón central.
pyautogui.doubleClick() # Simula un doble clic con el botón izquierdo.
#%%----> Mover el mouse con click sostenido
pyautogui.dragRel() # movimiento en referencia a la ultima posición
pyautogui.dragTo()  # movimiento en referencia a coordenadas
#%%
# correr el programa y abrir paint en menos de 5seg
import pyautogui, time
time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

#%%
# correr el programa y abrir paint en menos de 5seg
import pyautogui, time
time.sleep(5)
j = 0
for i in range(3):
    print("Vuelta %d"%i)
    pyautogui.click()
    pyautogui.dragTo(400+j, 400+j, duration=0.15)
    pyautogui.dragTo(500+j, 400+j, duration=0.15)
    pyautogui.dragTo(500+j, 500+j, duration=0.15)
    pyautogui.dragTo(400+j, 500+j, duration=0.15)
    j = j + 20
#%%----> Scrolling
import time, pyautogui
pyautogui.scroll(200)
time.sleep(1); pyautogui.scroll(100)
#%%----> Captura de pantalla
import pyautogui 
im = pyautogui.screenshot ()
# en el pixel de coordenadas (0,0) se tiene el RGB
print(im.getpixel((0, 0)))  
# en el pixel de coordenadas (50,200) se tiene el RGB
print(im.getpixel((50, 200)))
# pregunta si en la coordenada es igual al rgb en parentesis
print(pyautogui.pixelMatchesColor(50, 200,(34, 43, 53)))
print(pyautogui.pixelMatchesColor(50, 200,(33, 43, 53)))
#%%----> TECLADO
pyautogui.click(100, 100)
for i in range(2):
    pyautogui.typewrite('\nHola Beta', 0.25)
pyautogui.typewrite(['\n','a', 'b', 'left', 'left', 'X', 'Y'],0.25)
#%%----> Tabla de Teclado
#   'a', 'b', ,..., 'z', '@', '#' -> escribe normal los caracteres
#   'enter', 'return', '\n'       -> Enter o salto de linea
#   'esc'                         -> ESC
#   'shiftleft', 'shiftright'     -> Izquierda o derecha SHIFT
#   'altleft', 'altright'         -> Izquierda o derecha ALT
#   'ctrlleft', 'ctrlright'       -> Izquierda o derecha CTRL
#   'tab' (or '\t')               -> The TAB key
#   'backspace', 'delete'         -> The BACKSPACE and DELETE keys
#   'pageup', 'pagedown'          -> The PAGE UP and PAGE DOWN keys
#   'home', 'end'                 -> The HOME and END keys
#   'up', 'down', 'left', 'right' -> The up, down, left, and right arrow keys
#   'f1', 'f2', 'f3'              -> and so on The F1 to F12 keys
#   'volumemute', 'volumedown', 'volumeup' -> The mute, volume down, volume up
#   'pause'                       -> The PAUSE key
#   'capslock', 'numlock'         -> The CAPS LOCK, NUM LOCK
#   'scrolllock'                  -> SCROLL LOCK
#   'insert'                      -> The INS or INSERT key
#   'printscreen'                 -> The PRTSC or PRINT SCREEN key
#   'winleft', 'winright'         -> The left and right WIN keys (on Windows)
#   'command'                     -> The Command () key (on OS X) 
#   'option'                      -> The OPTION key (on OS X)
#%%----> Presion de teclado 
# pyautogui.keyDown() & pyautogui.keyUp() -> press()
pyautogui.click(100, 100)
pyautogui.keyDown('shift')
pyautogui.press('enter')
pyautogui.press('4')
pyautogui.keyUp('shift')
#%%----> combinación de comandos
# Proceso de control + v -> alargado
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
# Proceso de control + v -> corto
pyautogui.hotkey('ctrl', 'c')
#%%----> Recuento de funciones
# moveTo(x, y)
# moveRel(xOffset, yOffset)
# dragTo(x, y)
# dragRel(xOffset, yOffset)
# click(x, y, button)
# rightClick()
# middleClick()
# doubleClick()
# mouseDown(x, y, button)
# mouseUp(x, y, button)
# scroll(units)
# typewrite(message)
# typewrite([key1, key2, key3])
# press(key)
# keyDown(key)
# keyUp(key)
# hotkey([key1, key2, key3])
# screenshot()
#%%---->



#%%---->



#%%---->



