##
## image_embedsを画像に戻す
##

from diffusers import StableUnCLIPImg2ImgPipeline
from diffusers.utils import load_image
import torch
import os, json, random
from PIL import Image
import numpy as np

#root_dir = r"C:\Users\1000001991\Desktop\RSM_Imagine\dataset_v5"
root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5"


def unclip_50_main(pipe):
    target = '00_beer_bottle'

    top_dir = os.path.join(root_dir, target)
    image_embeds_dir = os.path.join(top_dir, '22_image_embeds')
    output_dir = os.path.join(top_dir, '31_variation_16x16_image_embeds')
    os.makedirs(output_dir, exist_ok=True)


    for i in range(16):
        id_0 = str(i).zfill(2)
        image_embeds_0 = np.load(os.path.join(image_embeds_dir, f'{id_0}.npy'))

        for j in range(16):
            id_1 = str(j).zfill(2)
            image_embeds_1 = np.load(os.path.join(image_embeds_dir, f'{id_1}.npy'))

            mean = (image_embeds_0 + image_embeds_1) / 2
            print("SHAPE OF MEAN : {}".format(mean.shape))
            mean = torch.tensor(mean, dtype=torch.float16).to("cuda")

            image = pipe(image_embeds=mean).images[0]
            image.save(os.path.join(output_dir, f'{id_0}_{id_1}.jpg'))

if __name__ == "__main__":
    unclip_50_main()