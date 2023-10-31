##
##画像からimage_embedsを抽出
##

from PIL import Image
import os, glob
import torch
import numpy as np
from transformers import AutoProcessor, CLIPVisionModelWithProjection

root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_Imagine\RSM_imagine_dataset_v5"

data_dir = os.path.join(root_dir, 'data')

def main():
    target = '00_beer_bottle'
    # target = '01_interior'
    #  target = '02_painting'

    top_dir = os.path.join(data_dir, target)
    image_dir = os.path.join(top_dir, '10_good_image')
    image_embeds_dir = os.path.join(top_dir, '22_image_embeds')
    os.makedirs(image_embeds_dir, exist_ok=True)

    model_name = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
    model = CLIPVisionModelWithProjection.from_pretrained(model_name).to('cuda', dtype=torch.float16)
    processor = AutoProcessor.from_pretrained(model_name)

    for i in range(16):
        id = str(i).zfill(2)
        image = Image.open(os.path.join(image_dir, f'{id}.jpg'))
        clip_image = processor(images=image, return_tensors="pt").pixel_values
        image_embeds = model(clip_image.to('cuda', dtype=torch.float16)).image_embeds

        print(i, image_embeds.shape, image_embeds.dtype)
        image_embeds = image_embeds.to(torch.float32)
        print(i, image_embeds.shape, image_embeds.dtype)
        np.save(os.path.join(image_embeds_dir, f'{id}.npy'), image_embeds.to('cpu').detach().numpy())
    print("Main() done.")

def clip_image_vector_30_main2(model, processor):
    ##########TAKES A WHILE TO LOAD#####
    #model_name = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
    #model = CLIPVisionModelWithProjection.from_pretrained(model_name).to('cuda', dtype=torch.float16)
    #processor = AutoProcessor.from_pretrained(model_name)
    ####################################

    root_folder = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\00_beer_bottle"
    in_folder = os.path.join(root_folder, '30_variation_16x16')
    out_folder = os.path.join(root_folder, '42_variation_image_embeds')

    print("in_folder is {}".format(str(in_folder)))
    print("out_folder is {}".format(str(out_folder)))


    for path in glob.glob(os.path.join(in_folder, '*')):
        print("Path is {}".format(path))
        basename = os.path.splitext(os.path.basename(path))[0]
        print(basename)

        image = Image.open(path)
        clip_image = processor(images=image, return_tensors="pt").pixel_values
        image_embeds = model(clip_image.to('cuda', dtype=torch.float16)).image_embeds

        print(basename, image_embeds.shape, image_embeds.dtype)
        image_embeds = image_embeds.to(torch.float32)
        print(basename, image_embeds.shape, image_embeds.dtype)
        np.save(os.path.join(out_folder, f'{basename}.npy'), image_embeds.to('cpu').detach().numpy())

    print("Main2() done.")
if __name__ == "__main__":
    clip_image_vector_30_main2()