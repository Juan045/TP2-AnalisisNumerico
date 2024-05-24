#import matplotlib.pyplot as plt
import graficarImg as gr
import numpy as np
import cv2

def ejercicioA(img1BGR, img2BGR):
    # pasar las imagenes de RGB a HSV
    img1HSV = cv2.cvtColor(img1BGR[:,:,[2,1,0]], cv2.COLOR_RGB2HSV)
    img2HSV = cv2.cvtColor(img2BGR[:,:,[2,1,0]], cv2.COLOR_RGB2HSV)
    
    # elegir los umbrales minimos y maximos del amarillo
    # TENEMOS QUE DETERMINAR BIEN EL MINIMO Y EL MAXIMO
    amarilloMin = np.array([20, 30, 42])
    amarilloMax = np.array([80, 255, 255])
    
    # crear la mascara
    mascara = cv2.inRange(img1HSV, amarilloMin, amarilloMax)
    
    return mascara
    
def main():
    # cargar imagenes
    # cv2 las carga en formato BGR
    img1BGR = cv2.imread('im1_tp2.jpg')
    img2BGR = cv2.imread('im2_tp2.jpg')

    img1HSV = cv2.cvtColor(img1BGR[:,:,[2,1,0]], cv2.COLOR_RGB2HSV)
    # A -----------------
    # Convierta las imagenes al espacio de color HSV. Determine umbrales, minimos y maximos, en el canal
    # de matiz (H) para el color amarillo y cree una mascara.
    mascara = ejercicioA(img1BGR, img2BGR)
    
    # B -----------------
    # aplicar la mascara al canal de saturacion (S), y utilizar una matriz de convolucion conveniente para
    # detectar los bordes de la imagen resultante.
    resultado = cv2.bitwise_and(img1HSV[:,:,1], img1HSV[:,:,1], mask=mascara)
    gr.plotHSV(resultado)
    
main()