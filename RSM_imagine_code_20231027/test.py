from PIL import Image
import os, cv2, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

FIRST_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\00.jpg"
SECOND_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\01.jpg"
THIRD_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\02.jpg"



img1 = mpimg.imread(FIRST_DIR)
img2 = mpimg.imread(SECOND_DIR)
img3 = mpimg.imread(THIRD_DIR)

while True:
    for i in np.arange(0, 1.1, 0.1):
            ratio = i /100
            img = cv2.addWeighted(img1, (1-i), img2, i, 0.0)
            #time.sleep(0.5)
            plt.imshow(img)
            plt.axis('off')
            plt.show(block=False)
            plt.pause(0.01)
    
    for i in np.arange(0, 1.1, 0.1):
            ratio = i /100
            img = cv2.addWeighted(img2, (1-i), img3, i, 0.0)
            #time.sleep(0.5)
            plt.imshow(img)
            plt.axis('off')
            plt.show(block=False)
            plt.pause(0.01)

    for i in np.arange(0, 1.1, 0.1):
            ratio = i /100
            img = cv2.addWeighted(img3, (1-i), img1, i, 0.0)
            #time.sleep(0.5)
            plt.imshow(img)
            plt.axis('off')
            plt.show(block=False)
            plt.pause(0.01)