import matplotlib.pyplot as plt

# funciones para poder hacer las graficas y visualizar los puntos que realizamos en app.py

def plotRGB(img, title = ''):
    plt.title(title)
    plt.imshow(img[:,:,[2,1,0]])
    plt.show()

def plotHSV(img, title = ''):
    plt.title(title)
    plt.imshow(img)
    plt.show()

def plotHSVMul2tImg(img1, img2, title='', t1='', t2=''):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle(title, fontsize=16)
    
    
    axes[0].imshow(img1, cmap='gray')
    axes[0].set_title(t1)
    axes[0].axis('on')
        
    axes[1].imshow(img2, cmap='gray')
    axes[1].set_title(t2)
    axes[1].axis('on')
    
    plt.show()

def plotHSVMultImg(img1, img2, img3, img4, title='',t1='',t2='',t3='',t4=''):
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle(title, fontsize=16)
    
    axes[0, 0].imshow(img1)
    axes[0, 0].set_title(t1)
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(img2)
    axes[0, 1].set_title(t2)
    axes[0, 1].axis('off')
    
    axes[1, 0].imshow(img3)
    axes[1, 0].set_title(t3)
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(img4)
    axes[1, 1].set_title(t4)
    axes[1, 1].axis('off')
    
    plt.show()

