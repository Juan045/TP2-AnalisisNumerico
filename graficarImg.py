import matplotlib.pyplot as plt


def plotRGB(img, title = ''):
    plt.title(title)
    plt.imshow(img[:,:,[2,1,0]])
    plt.show()

def plotHSV(img, title = ''):
    plt.title(title)
    plt.imshow(img)
    plt.show()