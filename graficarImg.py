import matplotlib.pyplot as plt


def plotRGB(img):
    plt.imshow(img[:,:,[2,1,0]])
    plt.show()

def plotHSV(img):
    plt.imshow(img)
    plt.show()