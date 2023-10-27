from transformers import InstructBlipProcessor, InstructBlipForConditionalGeneration
import torch
from PIL import Image
import requests
import os, glob

model = InstructBlipForConditionalGeneration.from_pretrained("Salesforce/instructblip-flan-t5-xl", torch_dtype=torch.float16)
processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-flan-t5-xl", torch_dtype=torch.float16)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


image_dir = r"C:\Users\1000001991\Desktop\RSM_imagine\dataset_v5\RSM_imagine_dataset_v5\00_beer_bottle\10_good_image"
responses = []
for path in glob.glob(os.path.join(image_dir, '*')):
    basename = os.path.splitext(os.path.basename(path))[0]
    image = Image.open(path).convert("RGB")

    prompt = "Without using words such as symbolic or vintage, give the most characteristic word to describe the design and atmosphere of a beer bottle label."
    inputs = processor(images=image, text=prompt, return_tensors="pt").to(device)

    outputs = model.generate(
            **inputs,
            do_sample=False,
            num_beams=5,
            max_length=256,
            min_length=1,
            top_p=0.9,
            repetition_penalty=1.5,
            length_penalty=1.0,
            temperature=1,
    )
    generated_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
    print(basename, generated_text)
    responses.append(generated_text)


test = [
    'The beer bottle label in the image has a vintage design and atmosphere, which is characteristic of a well-crafted beer bottle label. The label features a black background with gold lettering, which creates a sense of elegance and sophistication. The label also features an ornate design, which adds to the overall aesthetic appeal of the bottle.',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is rustic. This word can be used to describe the overall look and feel of the label, as well as the type of beer it contains. The label features a brown bottle with an image of a deer on it, which creates a rustic and natural atmosphere. The label also has a white background, which adds a subtle contrast to the dark brown color of the beer bottle.',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is rustic. This word can be used to describe the design and atmosphere of a beer bottle label that incorporates natural elements, such as trees, leaves, and grasses, to create a rustic, natural, and authentic atmosphere.',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a design or atmosphere that has been around for a long time, especially one that has been used for a long period of time, such as in the case of a beer bottle label. Vintage can also be used to describe a design or atmosphere that has been around for a long time, such as in the case of a beer bottle label. Vintage can also be used to describe a design or atmosphere that has been around for a long time, such as in the case of a beer bottle label.',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been around for a long time, especially in the case of a beer bottle label. Vintage can be used to describe a design or atmosphere that has been',
    'The design and atmosphere of a beer bottle label can be described as rustic, which is characterized by the use of natural elements, such as plants, trees, and grasses, to convey a sense of nature, authenticity, and authenticity. The bottle label in the image features a green bottle with a white label, which creates a rustic and natural atmosphere.',
    'The design and atmosphere of the label on the bottle of Apipa beer can be described as rustic. The bottle is decorated with a rustic-inspired design, featuring a tree-shaped label with a leafy pattern. The label also features a wooden background, which adds a rustic touch to the overall design and atmosphere of the bottle. The bottle is placed on a white background, which creates a neutral and unobtrusive setting for the beer.',
    'The design and atmosphere of a beer bottle label can be described as rustic, which is characterized by the use of natural elements, such as wood, stone, and greenery, to create a warm, inviting, and rustic atmosphere. The label of the beer bottle in the image features a dark brown background with a black lettering that reads "IPA" on a white background. The design of the label resembles a rustic farmhouse, which is a characteristic feature of IPA beers, which are known for their rich, complex flavors and distinctive aromas.',
    'The design and atmosphere of a beer bottle label can be described using the word rustic, which is a combination of the words rustic and vintage. A rustic beer bottle label has a simple, rustic design, featuring a brown background with a black lettering on the label. This type of label is often used to promote a specific brand or product, such as a local brewery or a craft brewery. The rustic design of the label creates a warm and inviting atmosphere, making it a perfect choice for a beer bottle label.',
    "The design and atmosphere of the label on the beer bottle are characterized by a dark, rich, and elegant atmosphere. The label features a black background with a gold lettering, which creates a sense of elegance and sophistication. The label also features an image of an octopus, which is a common motif for beer bottle labels. The octopus can be used as a symbol of good luck, prosperity, and good fortune. It can also be used as a metaphor for a person's life journey, as it symbolizes a person's ability to overcome obstacles and achieve their goals. The beer bottle label in the image features a black background with a gold lettering, which creates a sense of elegance and sophistication. The label also features an image of an octopus, which is a common motif for beer bottle labels. The octopus can be used as a symbol of good luck, prosperity, and good fortune. It can also be used as a metaphor for a person's life journey, as it symbolizes a person's ability to overcome obstacles and achieve their goals. The beer bottle label in the image",
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label. Vintage is a term used to describe a style that has been around for a long period of time, and it can be used to describe the design and atmosphere of a beer bottle label.',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design or atmosphere that has been around for',
    'The most characteristic word to describe the design and atmosphere of a beer bottle label is vintage. Vintage refers to a style that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the beer bottle label in the image. Vintage can be used to describe a design that has been around for a long period of time, such as in the case of the',
    'The design and atmosphere of a beer bottle label can be described as rustic, which is characterized by the use of natural elements, such as wood, stone, and leaves, to create a warm and inviting atmosphere. The bottle label in the image features an orange background with a white lettering that reads "IPA", indicating that the beer is brewed in the United States. The label also features a black and white image of a leaf, which adds a sense of authenticity to the design and atmosphere of the beer bottle label.'
    ]

test2 = [
    {0, "Sophisticated", "洗練"},
    {1, "Rustic", "素朴"},
    {2, "", ""},
    {3, "Elegant", "華やかな"},
    {4, "Active", "アクティブ"},
    {5, "Plain", "簡素"},
    {6, "Natural", "自然"},
    {7, "Modest", "控えめ"},
    {8, "Stable", "安定感"},
    {9, "Safe", "無難"},
    {10, "Formal", "フォーマル"},
    {11, "Modern", "モダン"},
    {12, "Romantic", "ロマンティック"},
    {13, "Mannish", ""},
    {14, "Artificial", ""},
    {15, "Simple", ""}
]

print("==============")
print(responses)
