from PIL import Image
import os, cv2, time, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


first_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\00.jpg"
SECOND_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\01.jpg"
THIRD_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image\02.jpg"


    
## datasets available: landscape, fashion, beer, interior
print("This is the name of the program:", sys.argv[0])
print("Dataset type", sys.argv[1])





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