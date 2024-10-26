import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
import openpyxl
import pyautogui
from time import sleep
import traceback  # Importando o módulo traceback

i = 0
quantidade = 10000
cont_geral = 0

 
def gera_doc_google():
    #icone_foto = pyautogui.locateCenterOnScreen('icone_foto.png', confidence=0.98)
    #pyautogui.click(icone_foto.x, icone_foto.y)
    sleep(0.2)
    #clicar com o botao direito
    #pyautogui.click(button='right')
    #sleep(0.3)

    pyautogui.hotkey('shift', 'F10')
    sleep(0.5)    

    #abrir com
    abrir_com = pyautogui.locateCenterOnScreen('abrir_com.png', confidence=0.7)
    pyautogui.click(abrir_com.x, abrir_com.y)
    sleep(1)

    #doc google
    doc_google = pyautogui.locateCenterOnScreen('doc_google.png', confidence=0.9)
    pyautogui.click(doc_google.x, doc_google.y)
    sleep(1)

def volta_guia():
    print("Voltando a guia anterior")
    pyautogui.hotkey('ctrl', '2')
    sleep(1)

input("Pressione Enter para começar a execução...")

try:
    while i < quantidade:
        if i == 0:
            icone_foto = pyautogui.locateCenterOnScreen('icone_foto.png', confidence=0.95)
            pyautogui.click(icone_foto.x, icone_foto.y)
            gera_doc_google()
            sleep(2)
            pyautogui.hotkey('ctrl', 'w')
        else:
            volta_guia()
            pyautogui.press('down')
            sleep(0.8)
            gera_doc_google()
            sleep(2)
            pyautogui.hotkey('ctrl', 'w')
        i += 1

        cont_geral += 1
    
except Exception as e:
    print("Ocorreu um erro:")
    traceback.print_exc()  # Imprime o traceback completo da exceção

finally:
    input("Pressione Enter para sair...")
