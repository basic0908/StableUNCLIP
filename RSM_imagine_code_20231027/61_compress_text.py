import openai
import os, json, random, re
from PIL import Image, ImageFont, ImageDraw

root_dir = r"C:\Users\1000001991\Desktop\RSM_imagine"
root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_Imagine"


output_dir = os.path.join(root_dir, 'LLM_refine')

prompt_estimate_group_name = """# Description Analysis
Analyze the description and respond by extracting the single most symbolic word that best describes the characteristics of the beer bottle label.

## Description
"""


descs = [
"The most appropriate and symbolic word to describe the characteristics of a beer bottle label is vintage. Vintage is an appropriate and symbolic word to describe the characteristics of a beer bottle label, as it represents the quality and authenticity of the product, as well as the time and effort that went into its creation. Vintage is also a term that can be used to refer to a type of beer that has been around for a long period of time, such as a craft beer or a traditional IPA. Vintage is also a term that can be used to describe a type of beer that has been around for a long period of time, such as a craft beer or a traditional IPA. In the image, there is a bottle of IPA sitting on a gray background with a vintage label on it. Vintage is a term that can be used to describe a type of beer that has been around for a long period of time, such as a craft beer or a traditional IPA. Vintage is also a term that can be used to describe a type of beer that has been around for a long period of time, such as a craft beer or a traditional IPA.",
"The most appropriate and symbolic word to describe the characteristics of a beer bottle label is rustic. This word can be used to describe the appearance of the label, which features an image of an elk on a gray background. The elk is a symbol of strength, power, and endurance, which can be used to convey a sense of authenticity, integrity, and quality. The elk's presence on the label adds a sense of authenticity to the image, as well as a sense of authenticity to the beer itself. In addition, the elk's presence on the label provides a sense of authenticity to the beer itself, as it is a representation of the elk's role in the elk's natural habitat. Therefore, the elk's presence on the label represents the elk's role in the elk's natural habitat, as well as its importance in the elk's natural habitat."
"The most appropriate and symbolic word to describe the characteristics of a beer bottle label is symbolic. This word can be used to describe the characteristics of a beer bottle label, such as its shape, size, color, and design. It can also be used to describe the characteristics of a beer, such as its taste, aroma, and appearance. For example, the beer bottle label in the image depicts an image of a tree, which can be used as a symbol of nature, harmony, and balance."
"The most appropriate and symbolic word to describe the characteristics of a beer bottle label is vintage. Vintage is an appropriate and symbolic word to describe the characteristics of a beer bottle label, as it reflects the quality and authenticity of the product, as well as the time and effort that went into its creation. Vintage is also a term that can be used to refer to a specific type of beer, such as a wheat beer or a pilsner beer. These types of beers are typically aged for a longer period of time, resulting in more complex flavors and aromas. Vintage is also a term that can be used to refer to a specific type of beer, such as a wheat beer or a pilsner beer. These types of beers are typically aged for a longer period of time, resulting in more complex flavors and aromas. Vintage is also a term that can be used to refer to a specific type of beer, such as a wheat beer or a pilsner beer. These types of beers are typically aged for a longer period of time, resulting in more complex flavors and aromas. Vintage is also a term that can be used"
    
]
04 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the characteristics of a beer, such as its taste, aroma, and appearance. For example, the label on the bottle of aa ipa contains the word "aa" or "aa ipa", which is a combination of the words "aa" and "ipa", indicating that it is a type of IPA beer. In this context, the word "symbolic" can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the characteristics of a beer, such as its taste, aroma, and appearance. For example, the label on the bottle of aa ipa contains the word "aa" or "aa ipa", which is a combination of the words "aa" and "ipa", indicating
05 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is logo. A beer bottle label is a visual representation of a company's brand identity, which can be used to communicate a company's values, mission, and vision to potential customers. The label of the beer bottle in the image features a white background with a black lettering that reads "pa pa." The lettering on the label represents the company's name, as well as the type of beer it produces, its target audience, and its marketing strategy. The lettering on the label also reflects the company's branding, which can be used to convey a company's personality, uniqueness, and distinctiveness.
06 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the characteristics of a beer, such as its taste, aroma, and appearance. For example, the beer bottle label in the image depicts a bottle with a label that reads "npmp", which is a combination of the words "npmp" and "ipmp". The combination of these two words creates a symbol that can be used to represent the characteristics of a beer bottle label, such as its shape, color, and design. In addition, the combination of these two words can be used to describe the characteristics of a beer, such as its taste, aroma, and appearance. For example, the beer bottle label in the image depicts a bottle with a label that reads "npmp", which is a combination of the words "npmp" and "ipmp". The combination of these two words creates a symbol that can be used to
07 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". Symbolic is a word that can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the meaning behind the label, such as its symbolism or meaning. For example, the label on the bottle of Apipa beer depicts an image of a tree, which can be used to represent the company's brand or identity. Similarly, the label on the bottle of Apipa beer depicts an image of a tree, which can be used to represent the company's brand or identity. Finally, the label on the bottle of Apipa beer depicts an image of a tree, which can be used to represent the company's brand or identity. Therefore, the label on the bottle of Apipa beer can be used to represent the company's brand or identity.
08 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the characteristics of the beer itself, such as its taste, aroma, and appearance. For example, the beer bottle label in the image depicts an IPA, which is a type of beer with a dark brown color and a greenish-yellow label. The greenish-yellow color on the label indicates that the beer is brewed with green hops, while the greenish-yellow label indicates that the beer is brewed with black hops. These characteristics can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. For example, the beer bottle label in the image depicts an IPA, which is a type of beer with a dark brown color and a greenish-yellow label. These characteristics can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design
09 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is vintage. Vintage is an appropriate and symbolic word to describe the characteristics of a beer bottle label, as it refers to a design that has been passed down from generation to generation, resulting in a sense of authenticity and quality. Vintage can also be used to describe a type of beer, such as a craft beer, that has been aged for a long period of time, resulting in a distinctive taste and aroma. Vintage can also be used to describe a type of beer, such as a dark beer, that has been aged for a long period of time, resulting in a distinctive taste and aroma.
10 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the appearance of the label, which features an image of an octopus on a black background. The octopus is a symbol of good luck, prosperity, and good fortune, and it is often used to signify good luck, good fortune, and good fortune. The octopus on the label represents good luck, prosperity, and good fortune. It can also be used as a metaphor for good luck, good fortune, and good fortune. The octopus on the label represents good luck, prosperity, and good fortune, and it can also be used as a metaphor for good luck, good fortune, and good fortune. The octopus on the label represents good luck, prosperity, and good fortune, and it can also be used as a metaphor for good luck, good fortune, and good fortune. The octopus on the label represents good luck, prosperity, and good fortune, and it can also be used as a metaphor for good luck, good fortune, and good
11 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. It can also be used to describe the meaning behind the label, such as the company's name, the brewery's name, or the type of beer it is. For example, the beer bottle label in the image contains the word "IPA" (IPA stands for "Irish Pale Ale"), which is a type of beer with a dark brown color and a gold-colored logo on the label. This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. For example, the beer bottle label in the image contains the word "IPA" (IPA stands for "Irish Pale Ale"), which is a type of beer with a dark brown color and a gold-colored logo on the label. This word can be used to describe the characteristics of a beer bottle label, such as its shape, color, and design. For example, the beer bottle
12 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is vintage. Vintage is a term used to describe the characteristics of a beer bottle label, such as its style, design, and overall aesthetic. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer. Vintage can also be used to refer to a specific type of beer, such as a wheat beer or a sour beer.
13 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the appearance of a beer bottle label, as well as its meaning and significance. For example, a beer bottle label with the word "IPA" on it may represent a specific type of beer, such as a wheat beer, a pale ale, or a stout. The label may also represent a particular brand or style of beer, such as a craft beer or an IPA. A beer bottle label with the word "IPA" on it may represent a specific type of beer, such as a wheat beer, a pale ale, or a stout. The label may also represent a particular brand or style of beer, such as a craft beer or an IPA. In the image, there is a beer bottle label with the word "IPA" on it that is sitting on a gray surface. The label may represent a specific type of beer, such as a wheat beer, a pale ale, or a stout. The label may also represent
14 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as its shape, size, color, and design. It can also be used to describe the characteristics of a brand, such as IPA, which represents a specific type of beer. In the image, there is an IPA beer bottle label on a gray background with a white background. The label contains the word "ipa", which is a common abbreviation for the International Pale Ale Association (IPA). The word "ipa" can be used to describe the characteristics of a beer bottle label, such as its shape, size, color, and design. It can also be used to describe the characteristics of a brand, such as IPA, which represents a specific type of beer. In the image, there is an IPA beer bottle label on a gray background with a white background. The label contains the word "ipa", which is a common abbreviation for the International Pale Ale Association (IPA). The word "i
15 The most appropriate and symbolic word to describe the characteristics of a beer bottle label is "symbolic" or "symbolic". This word can be used to describe the characteristics of a beer bottle label, such as the color of the bottle, the design of the label, and the presence of a leaf on the label. It can also be used to describe the characteristics of the beer itself, such as the type of beer, the country of origin, and the region in which the beer was brewed."

class GPT:
    def __init__(self):
        openai.api_key = "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"

    def response(self, prompt):
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                max_tokens=2048,
                prompt=prompt
            )

        except Exception as e:
            return f"Exception: {e.args}"
       
        return response['choices'][0]['text']

def main():
    gpt = GPT()
    # template_prompt = prompt_estimate_group_name_for_landscape.replace('{GENRE}', genre)
    template_prompt = prompt_estimate_group_name.replace('{GENRE}', genre)

    json_path = os.path.join(root_dir, 'dataset_v5', 'data', category_name, 'good_styles.json')
    with open(json_path, 'r') as json_file:
        good_styles = json.load(json_file)

    report = {
        'genre': genre,
        'category_name': category_name,
        'template_prompt': template_prompt,
        'samples': []
    }

    loop_num = 45

    for l in range(loop_num):
        random_styles = random.sample(good_styles['styles'], random.randint(1, 4))

        requests = []
        caption_list = ''
        for s, style in enumerate(random_styles):
            last = '\n'
            if s == len(random_styles) - 1:
                last = ''
            caption_list = caption_list + style['BLIP_caption'] + last
            requests.append(style['BLIP_caption'])

        print('\n', l)

        prompt = template_prompt + caption_list
        print(prompt)

        response = gpt.response(prompt)
        response = response.replace("\n", "")

        print(response)

        report['samples'].append({
            'requests': requests,
            'response': response
        })

    with open(os.path.join(output_dir, f'samples_{category_name}.json'), "w") as json_file:
        json.dump(report, json_file, indent=2)

if __name__ == "__main__":
    main()
