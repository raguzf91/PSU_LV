from matplotlib import pyplot as plt
import numpy as np

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

img_array=[]

img_array=img+0.6
img_array[img_array>1]=1

img1 = np.rot90(img,3) 
img2 = np.fliplr(img) 
img3 = img[::5,::5] 

redovi = img.shape[0]
stupci = img.shape[1]

dg = stupci//4
gg = stupci//2


pr_img = img.copy()
for i in range(redovi):
    for j in range(stupci):
        if (j < dg or j > gg): 
            pr_img[i][j] = 0

plt.figure(1)
plt.title("a) brightness")
plt.imshow(img_array,cmap='gray')

plt.figure(2)
plt.title("b) rotirana slika")
plt.imshow(img1,cmap='gray')

plt.figure(3)
plt.title("c) zrcaljena slika")
plt.imshow(img2,cmap='gray')

plt.figure(4)
plt.title("d) smanjena kvaliteta slike")
plt.imshow(img3,cmap='gray')

plt.figure(5)
plt.title("e) stupci")
plt.imshow(pr_img, cmap='gray')

plt.show()