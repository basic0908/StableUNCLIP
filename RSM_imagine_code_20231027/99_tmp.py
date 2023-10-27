import os, json, glob

root_dir = r"C:\Users\1000001991\Desktop\RSM_Imagine\dataset_v5"
data_dir = os.path.join(root_dir, 'data')

def main2():
    target = '02_painting'

    top_dir = os.path.join(data_dir, target)
    with open(os.path.join(top_dir, 'all_styles.json'), 'r') as json_file:
        all_styles = json.load(json_file)

    with open(os.path.join(top_dir, 'good_styles.json'), 'r') as json_file:
        good_styles = json.load(json_file)

    for s, styles in enumerate(good_styles['styles']):
        for alls in all_styles['styles']:
            if styles['name'] == alls['name']:
                good_styles['styles'][s]['artist'] = alls['artist']

    with open(os.path.join(top_dir, 'good_styles_v2.json'), 'w') as json_file:
        json.dump(good_styles, json_file, indent=2, ensure_ascii=False)


def main():
    # target = '00_beer_bottle'
    # target = '01_interior'
    target = '02_painting'

    top_dir = os.path.join(data_dir, target)
    with open(os.path.join(top_dir, 'good_styles.json'), 'r') as json_file:
        good_styles = json.load(json_file)

    for s, styles in enumerate(good_styles['styles']):
        print(s, styles['name'])


if __name__ == "__main__":
    main2()
