import cv2
import numpy as np
from scipy import signal
import graficarImg as gr

def ejercicioA(imgBGR):


    # pasamos de BGR a HSV
    imgHSV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)
    
    # umbrales para el color amarillo
    amarilloMin = np.array([20, 41, 105])    
    amarilloMax = np.array([75, 255, 255])
            
    #  máscara
    mascara = cv2.inRange(imgHSV, amarilloMin, amarilloMax)
    
    return imgHSV, mascara

def main():
    
    img1BGR = cv2.imread('im1_tp2.jpg')
    img2BGR = cv2.imread('im2_tp2.jpg')
    
    # A: Conviertoa espacio de color HSV y creo la máscara
    img1HSV, mascara1 = ejercicioA(img1BGR)
    img2HSV, mascara2 = ejercicioA(img2BGR)
    gr.plotHSVMul2tImg(mascara1,mascara2,"","Mascara Imagen 1","Mascara imagen 2")
    gr.plotHSVMultImg(img1BGR[:,:,[2,1,0]],img1HSV,img2BGR[:,:,[2,1,0]],img2HSV,"","I1 RGB","I1HSV","I2RGB","I2HSV")
    
    # B: Aplico la máscara al canal  S
    canal_S1 = img1HSV[:, :, 1]
    resultado1 = cv2.bitwise_and(canal_S1, canal_S1, mask=mascara1)
    gr.plotHSV(resultado1, "Máscara aplicada en el canal de saturación (S) de I1")

    canal_S2 = img2HSV[:, :, 1]
    resultado2 = cv2.bitwise_and(canal_S2, canal_S2, mask=mascara2)
    gr.plotHSV(resultado2, "Máscara aplicada en el canal de saturación (S) de I2")
    
    # matriz de convolución, elegimos Sobel
    sobel_x = np.array([[ -1, 0, 1],
                        [ -2, 0, 2],
                        [ -1, 0, 1]])
    
    # convolución
    resultado_convolucion1 = signal.convolve2d(resultado1, sobel_x, mode='same', boundary='symm')
    resultado_convolucion2 = signal.convolve2d(resultado2, sobel_x, mode='same', boundary='symm')
    
    #  obtenemos una imagen de valores reales
    magnitud1 = np.abs(resultado_convolucion1).astype(np.uint8)
    magnitud2 = np.abs(resultado_convolucion2).astype(np.uint8)
    
  #  gr.plotHSV(magnitud1, "Resultado de la convolución entre el resultado (I1) y la matriz de convolución")
  #  gr.plotHSV(magnitud2, "Resultado de la convolución entre el resultado (I2) y la matriz de convolución")


#-------------------------------------------------------------------------------------------
    # C:
    # creamos un kernel
    kernel = np.ones((5, 5), np.uint8)
    
    # aca dilatamos los bordes encontrados
    dilatado1 = cv2.dilate(magnitud1, kernel, iterations=1)
    dilatado2 = cv2.dilate(magnitud2, kernel, iterations=1)
    
    # operación de cierre
    cerrado1 = cv2.morphologyEx(dilatado1, cv2.MORPH_CLOSE, kernel)
    cerrado2 = cv2.morphologyEx(dilatado2, cv2.MORPH_CLOSE, kernel)
    
  #  gr.plotHSV(cerrado1, "Resultado después de dilatación y cierre (I1)")
  #  gr.plotHSV(cerrado2, "Resultado después de dilatación y cierre (I2)")

    gr.plotHSVMultImg(magnitud1,cerrado1,magnitud2,cerrado2,"Punto C","Bordes resultantes de la I1","Area cerrada con frontera unica y conexa I1","Bordes resultantes de la I2","Area cerrada con frontera unica y conexa I2")

#---------------------------------------------------------------------------------------------
   # D
    # Encontramos los contornos
    contornos1, _ = cv2.findContours(cerrado1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos2, _ = cv2.findContours(cerrado2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Rellenamos 
    filled1 = cv2.drawContours(np.zeros_like(cerrado1), contornos1, -1, (255), thickness=cv2.FILLED)
    filled2 = cv2.drawContours(np.zeros_like(cerrado2), contornos2, -1, (255), thickness=cv2.FILLED)
    
    # Calcula area del color amarillo
    area_amarillo1 = np.sum(filled1 > 0)
    area_amarillo2 = np.sum(filled2 > 0)
    
    # Calcula area total de la imagen
    area_total1 = img1BGR.shape[0] * img1BGR.shape[1]
    area_total2 = img2BGR.shape[0] * img2BGR.shape[1]

    # Determino la proporcion de area amarilla
    proporcion_amarillo1 = area_amarillo1 / area_total1
    proporcion_amarillo2 = area_amarillo2 / area_total2
    
    print(f"Proporción de área amarilla en I1: {proporcion_amarillo1:.2%}")
    print(f"Proporción de área amarilla en I2: {proporcion_amarillo2:.2%}")

    gr.plotHSVMultImg(cerrado1,filled1,cerrado2,filled2,"","Frontera conexa resultantes de la I1","Bordes con area rellena I1","Frontera conexa resultantes de la I2","Bordes con area rellena I2")
    
#------------------------------------------------------------------------------
# E
    # Convertimos las áreas llenas a una máscara
    mascara_filled1 = filled1 > 0
    mascara_filled2 = filled2 > 0
    
    # Aplico la mascara a la imagen HSV original para obtener los valores de intensidad de amarillo
    intensidad_amarillo1 = np.sum(img1HSV[:, :, 2][mascara_filled1])
    intensidad_amarillo2 = np.sum(img2HSV[:, :, 2][mascara_filled2])
    
    print(f"Intensidad total de amarillo en I1: {intensidad_amarillo1}")
    print(f"Intensidad total de amarillo en I2: {intensidad_amarillo2}")

    # Determino la img con mas cantidad de muestra de amarillo
    if intensidad_amarillo1 > intensidad_amarillo2:
        print("I1 tiene más cantidad de muestra de amarillo.")
    else:
        print("I2 tiene más cantidad de muestra de amarillo.")
    

if __name__ == "__main__":
    main()