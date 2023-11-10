import keyboard, sys
from clip_image_vector_30 import *
from unclip_50 import *
from unclip_text_variation_51 import *


def load():
    # Loads all required models  
    #torch.cuda.empty_cache()

    #Loading clip_image_vector_30.py models
    model_name_clip_image_vector_30 = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
    model_clip_image_vector_30 = CLIPVisionModelWithProjection.from_pretrained(model_name_clip_image_vector_30).to('cuda', dtype=torch.float16)
    processor_clip_image_vector_30 = AutoProcessor.from_pretrained(model_name_clip_image_vector_30)
    print("----LOADING COMPLETED FOR clip_image_vector_30 (1/3)----")

    #Loading unclip_50.py pipeline
    pipe_unclip_50 = StableUnCLIPImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1-unclip", torch_dtype=torch.float16
    )
    pipe_unclip_50 = pipe_unclip_50.to("cuda")
    print("----LOADING COMPLETED FOR unclip_50 (2/3)----")

    #Loading unclip_text_variation_51.py pipeline
    pipe_unclip_text_variation_51 = StableUnCLIPImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1-unclip", torch_dtype=torch.float16
    )
    pipe_unclip_text_variation_51 = pipe_unclip_text_variation_51.to("cuda")

    model_name_unclip_text_variation_51 = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
    text_model_unclip_text_variation_51 = CLIPTextModelWithProjection.from_pretrained(model_name_unclip_text_variation_51).to('cuda', dtype=torch.float16)
    text_tokenizer_unclip_text_variation_51 = AutoTokenizer.from_pretrained(model_name_unclip_text_variation_51)
    print("----LOADING COMPLETED FOR model_name_unclip_text_variation_51 (3/3)----")
    

    print("----GPU USED: {}----".format(torch.cuda.current_device()))

    return model_clip_image_vector_30, processor_clip_image_vector_30, pipe_unclip_50, pipe_unclip_text_variation_51, text_model_unclip_text_variation_51, text_tokenizer_unclip_text_variation_51
        
def main():

    root_dir = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5"

    print('##############LOADING MODELS##############')

    model_clip_image_vector_30, processor_clip_image_vector_30,\
        pipe_unclip_50, pipe_unclip_text_variation_51,\
            text_model_unclip_text_variation_51, text_tokenizer_unclip_text_variation_51 = load()
    
    print("##############INITIALIZING PROCESS##############")
    print("##############PRESS ESC TO END##############")

    while True:
   

        #press escape to end loop
        if keyboard.is_pressed('esc'):
            print("##############ENDING PROCESS##############")
            break

if __name__ == "__main__":
    main()