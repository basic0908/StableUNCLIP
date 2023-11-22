from PIL import Image
import os, cv2, time, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

EMBEDS_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\00.npy"
EMBEDS_DIR2 = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\01.npy"

SECOND_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\10_good_image\01.jpg"
THIRD_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\10_good_image\02.jpg"
FOURTH_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\10_good_image\03.jpg"

csv = r"C:\Users\ibara\OneDrive - 株式会社エヌ・ティ・ティ・データ経営研究所\008_NTT人情研\202310TASK\data\RealtimeGeneration\pred_emv_latest.csv"
OUTPUT_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\OUTPUT_DIR"


current = mpimg.imread(SECOND_DIR)
next = mpimg.imread(THIRD_DIR)
img3 = mpimg.imread(FOURTH_DIR)




while True:
    for i in np.arange(0, 1.1, 0.1):
            #time.sleep(0.5)
            plt.imshow(cv2.addWeighted(img1, (1-i), img2, i, 0))
            plt.axis('off')
            plt.show(block=False)
            plt.pause(0.01)
    
    next_image = cv2.imread(os.path.join(OUTPUT_DIR, 'next_image.jpg'))
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'current_image.jpg'), next_image)
