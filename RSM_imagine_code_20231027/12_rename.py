import os, json, glob

root_dir = r"C:\Users\1000001991\Desktop\RSM_Imagine\dataset_v5"
data_dir = os.path.join(root_dir, 'data')

def main():
    # target = '00_beer_bottle'
    # target = '01_interior'
    target = '02_painting'

    top_dir = os.path.join(data_dir, target)
    with open(os.path.join(top_dir, 'all_styles.json'), 'r') as json_file:
        all_styles = json.load(json_file)

    good_styles = {"styles": []}

    for p, path in enumerate(glob.glob(os.path.join(top_dir, '10_good_image', '*'))):
        id = os.path.splitext(os.path.basename(path))[0][:2]
        style_name = all_styles['styles'][int(id)]['name']
        print(id, style_name)

        os.rename(path, os.path.join(top_dir, '10_good_image', f'{str(p).zfill(2)}.jpg'))
        good_styles["styles"].append({
            'name': style_name,
            'prompt': all_styles['template']['prompt'].replace('{NAME}', style_name),
            'negative_prompt': all_styles['template']['negative_prompt'],
            'BLIP_caption': ''
            })

    with open(os.path.join(data_dir, target, 'good_styles.json'), 'w') as json_file:
        json.dump(good_styles, json_file, indent=2)


if __name__ == "__main__":
    main()
