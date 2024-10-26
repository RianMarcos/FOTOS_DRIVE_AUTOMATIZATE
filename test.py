import cv2
import numpy as np
import pyautogui

# Carregar a imagem de referência
img_ref = cv2.imread('icone_foto.png', cv2.IMREAD_GRAYSCALE)

# Capturar a tela
screenshot = pyautogui.screenshot()
img_screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# Criar um detector de características
orb = cv2.ORB_create()

# Encontrar os keypoints e descritores
kp1, des1 = orb.detectAndCompute(img_ref, None)
kp2, des2 = orb.detectAndCompute(img_screen, None)

# Criar um objeto de correspondência
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Encontrar correspondências
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Desenhar as correspondências (opcional)
img_matches = cv2.drawMatches(img_ref, kp1, img_screen, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Exibir a imagem com correspondências (opcional)
cv2.imshow('Matches', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
