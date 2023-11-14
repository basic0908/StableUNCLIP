from PIL import Image
import os, cv2, time, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

EMBEDS_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\00.npy"
EMBEDS_DIR2 = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\01.npy"

SECOND_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\01.jpg"
THIRD_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\02.jpg"
csv = r"C:\Users\ibara\OneDrive - 株式会社エヌ・ティ・ティ・データ経営研究所\008_NTT人情研\202310TASK\data\RealtimeGeneration\pred_emv_latest.csv"

embeds1 = np.load(EMBEDS_DIR)
embeds2 = np.load(EMBEDS_DIR2)

print(type(embeds1))
print(type(embeds2))

print(embeds1.shape)
print(embeds2.shape)

print(embeds1[:20])
print(embeds2[:20])







# while True:
#     for i in np.arange(0, 1.1, 0.1):
#             #time.sleep(0.5)
#             plt.imshow(cv2.addWeighted(img1, (1-i), img2, i, 0))
#             plt.axis('off')
#             plt.show(block=False)
#             plt.pause(0.01)
    
#     for i in np.arange(0, 1.1, 0.1):
#             #time.sleep(0.5)
#             plt.imshow(cv2.addWeighted(img2, (1-i), img3, i, 0))
#             plt.axis('off')
#             plt.show(block=False)
#             plt.pause(0.01)

#     for i in np.arange(0, 1.1, 0.1):
#             #time.sleep(0.5)
#             plt.imshow(cv2.addWeighted(img3, (1-i), img1, i, 0))
#             plt.axis('off')
#             plt.show(block=False)
#             plt.pause(0.01)