##
##テキストからtext_embedsを抽出
##

from diffusers import StableUnCLIPImg2ImgPipeline
import torch
import os, json, random
from PIL import Image
import numpy as np

from transformers import AutoTokenizer, CLIPTextModelWithProjection

root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_Imagine\RSM_imagine_dataset_v5"

data_dir = os.path.join(root_dir, 'data')

def main():
    target = '00_beer_bottle'
    top_dir = os.path.join(data_dir, target)
    output_dir = os.path.join(top_dir, '32_variation_16x16_prompt')

    with open(os.path.join(top_dir, 'all_styles.json'), 'r') as json_file:
        template = json.load(json_file)['template']

    with open(os.path.join(top_dir, 'good_styles.json'), 'r') as json_file:
        good_styles = json.load(json_file)

    pipe = StableUnCLIPImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1-unclip", torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda")

    model_name = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
    text_model = CLIPTextModelWithProjection.from_pretrained(model_name).to('cuda', dtype=torch.float16)
    text_tokenizer = AutoTokenizer.from_pretrained(model_name)

    for i in range(16):
        id_0 = str(i).zfill(2)
        style_0 = good_styles['styles'][i]['name']

        for j in range(16):
            id_1 = str(j).zfill(2)
            style_1 = good_styles['styles'][j]['name']

            prompt = template['prompt'].replace('{NAME}', f'{style_0} and {style_1}')
            print(prompt)

            prompt_ids = text_tokenizer(
                        prompt,
                        padding=True,
                        return_tensors="pt"
                        ).input_ids
            encoder_hidden_states = text_model(prompt_ids.to('cuda'))[0]

            image = pipe(image_embeds=encoder_hidden_states).images[0]
            image.save(os.path.join(output_dir, f'{id_0}_{id_1}.jpg'))

if __name__ == "__main__":
    main()