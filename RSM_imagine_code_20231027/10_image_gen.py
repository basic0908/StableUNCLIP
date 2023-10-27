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
    seeds = [-1, -1, -1, -1, -1]

    top_dir = os.path.join(data_dir, target)
    with open(os.path.join(top_dir, 'all_styles.json'), 'r') as json_file:
        all_styles = json.load(json_file)
    
    for s, style in enumerate(all_styles['styles']):
        print(s, style['name'])

    # with open(os.path.join(r"C:\Users\1000001991\Desktop\RSM_imagine\dataset_v4\words.json"), 'r') as json_file:
    #     words = json.load(json_file)['words']
    #     for word in words:
    #         all_styles['styles'].append({
    #             'name': word['en']
    #         })

    # with open(os.path.join(top_dir, 'all_styles.json'), 'w') as json_file:
    #     json.dump(all_styles, json_file, indent=2)

    image_dir = os.path.join(top_dir, '00_sample_image')
    os.makedirs(image_dir, exist_ok=True)

    for s, style in enumerate(all_styles['styles']):
        prompt = all_styles['template']['prompt'].replace('{NAME}', style['name']).replace('{ARTIST}', style['artist'])
        print(prompt)

        for se, seed in enumerate(seeds):
            image = generate_request(prompt, all_styles['template']['negative_prompt'], seed=seed)
            image = image.resize((768, 768))
            image.save(os.path.join(image_dir, f'{str(s).zfill(2)}_{str(se)}.jpg'))

if __name__ == "__main__":
    main()
