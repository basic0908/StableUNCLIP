import os, json
from PIL import Image
from clip_interrogator import Config, Interrogator

#root_dir = r"C:\Users\1000001991\Desktop\RSM_Imagine\dataset_v5"
root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_Imagine\RSM_imagine_dataset_v5"

data_dir = os.path.join(root_dir, 'data')

def main():
    # target = '00_beer_bottle'
    # target = '01_interior'
    target = '02_painting'
    
    top_dir = os.path.join(data_dir, target)
    image_dir = os.path.join(top_dir, '10_good_image')

    ci = Interrogator(Config(clip_model_name="ViT-H-14/laion2b_s32b_b79k"))

    with open(os.path.join(top_dir, 'good_styles.json'), 'r') as json_file:
        good_styles = json.load(json_file)

    for i in range(16):
        image = Image.open(os.path.join(image_dir, f'{str(i).zfill(2)}.jpg')).convert('RGB')
        interrogated = ci.interrogate_fast(image)
        print(i, interrogated)
        good_styles['styles'][i]['BLIP_caption'] = interrogated

    with open(os.path.join(top_dir, 'good_styles.json'), "w") as json_file:
        json.dump(good_styles, json_file, indent=2)

if __name__ == "__main__":
    main()
