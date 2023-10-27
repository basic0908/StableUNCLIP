import os, json
import requests
import base64
from io import BytesIO
from PIL import Image

root_dir = r"C:\Users\1000001991\Desktop\RSM_Imagine\dataset_v5"
data_dir = os.path.join(root_dir, 'data')

def generate_request(prompt, negative_prompt, seed):
    url = "http://localhost:7860/sdapi/v1/txt2img"

    txt2img_payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": 20,
        "width": 1024,
        "height": 1024,
        "seed": seed,
        "sd_model_checkpoint": "sd_xl_base_1.0.safetensors [31e35c80fc]",
        "sd_vae": "sdxl_vae.safetensors",
        "sampler_index": "DPM++ 2M Karras",
    }

    response = requests.post(url, json=txt2img_payload)
    return Image.open(BytesIO(base64.b64decode(response.json()['images'][0].split(',',1)[0])))

def main():
    # target = '00_beer_bottle'
    # target = '01_interior'
    target = '02_painting'

    top_dir = os.path.join(data_dir, target)
    output_dir = os.path.join(top_dir, '32_variation_16x16_prompt')

    with open(os.path.join(top_dir, 'all_styles.json'), 'r') as json_file:
        template = json.load(json_file)['template']

    with open(os.path.join(top_dir, 'good_styles_v2.json'), 'r') as json_file:
        good_styles = json.load(json_file)

    for i in range(16):
        id_0 = str(i).zfill(2)
        style_0 = good_styles['styles'][i]['name']

        for j in range(16):
            id_1 = str(j).zfill(2)
            style_1 = good_styles['styles'][j]['name']

            # prompt = template['prompt'].replace('{NAME}', f'{style_0} and {style_1}')
            prompt = template['prompt'].replace('{NAME}', f'{style_0} and {style_1}').replace('{ARTIST}', f"{good_styles['styles'][i]['artist']}, {good_styles['styles'][j]['artist']}")

            print(prompt)
            
            image = generate_request(prompt, template['negative_prompt'], seed=-1)
            image = image.resize((768, 768))
            image.save(os.path.join(output_dir, f'{id_0}_{id_1}.jpg'))

if __name__ == "__main__":
    main()