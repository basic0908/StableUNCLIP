from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image"

for i in range(9):
    path = os.path.join(root_dir, '0{}.jpg'.format(i))


    if os.path.exists(path): 
        img = mpimg.imread(path)

        plt.axis('off')
        plt.imshow(img)       
        plt.show(block=False)
        plt.pause(1.5)
plt.close()