import keyboard, sys, os
from clip_image_vector_30 import *
from unclip_50 import *
from unclip_text_variation_51 import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

EMBEDS_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\00.npy"
OUTPUT_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\OUTPUT_DIR"
PRED_EMV_LATEST = r"C:\Users\ibara\OneDrive - 株式会社エヌ・ティ・ティ・データ経営研究所\008_NTT人情研\202310TASK\data\RealtimeGeneration\pred_emv_latest.csv"


def embeds_to_image(pipe, embeds):
    embeds = np.load(EMBEDS_DIR)
    print(embeds)
    image = torch.tensor(embeds, dtype=torch.float16).to("cuda")

    image = pipe(image_embeds=image).images[0]
    output_path = os.path.join(OUTPUT_DIR, 'output_image.jpg')
    image.save(output_path)

def showImage(path):
    if os.path.exists(path):
        img = mpimg.imread(path)

        plt.axis('off')
        plt.imshow(img)
        plt.show(block=False)
        plt.pause(0.1)
    else:
        print("PATH NOT FOUND : {}".format(path))

def toEmbeds():
    global EMBEDS_DIR, PRED_EMV_LATEST
    arr = np.loadtxt(PRED_EMV_LATEST, delimiter=",")
    reshaped_arr = arr[-1, :].reshape(1, -1)
    
    np.save(EMBEDS_DIR, reshaped_arr)

def load(optional=False):
    # Loads all required models  
    torch.cuda.empty_cache()

    if optional:
        #Loading clip_image_vector_30.py models
        model_name_clip_image_vector_30 = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"
        model_clip_image_vector_30 = CLIPVisionModelWithProjection.from_pretrained(model_name_clip_image_vector_30).to('cuda', dtype=torch.float16)
        processor_clip_image_vector_30 = AutoProcessor.from_pretrained(model_name_clip_image_vector_30)
        print("----LOADING COMPLETED FOR clip_image_vector_30 (1/2)----")

        return model_clip_image_vector_30, processor_clip_image_vector_30, pipe_unclip_50
        
    else:
        #Loading unclip_50.py pipeline
        print('---- LOADING MODELS ----')

        pipe_unclip_50 = StableUnCLIPImg2ImgPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1-unclip", torch_dtype=torch.float16
        )
        pipe_unclip_50 = pipe_unclip_50.to("cuda")
        print("---- LOADING COMPLETED ----")
    
        print("---- GPU IN-USE: {} ----".format(torch.cuda.current_device()))

        return pipe_unclip_50


def main():
    global EMBEDS_DIR
    global OUTPUT_DIR
    
    #model_clip_image_vector_30, processor_clip_image_vector_30, pipe_unclip_50 = load(optional=True)
    pipe_unclip_50 = load()

    
    print("---- INITIALIZING PROCESS ----")
    print("---- END - ESC  PAUSE - P   RESUME - R ----")

    paused = False 

    while True:
   
        if not paused:
            toEmbeds()

            embeds_to_image(pipe_unclip_50, EMBEDS_DIR)
            showImage(os.path.join(OUTPUT_DIR, 'output_image.jpg'))

            #press escape to end loop
            if keyboard.is_pressed('esc'):
                print("---- ENDING PROCESS ----")
                sys.exit(0)

            if keyboard.is_pressed('p'):
                keyboard.block_key(1)
                print('---- PAUSED ----')
                paused = True
            
        if paused:
            if keyboard.is_pressed('r'):
                keyboard.block_key(1)
                print('---- RESUMED ----')
                paused = False
            if keyboard.is_pressed('esc'):
                print("---- ENDING PROCESS ----")
                sys.exit(0)

if __name__ == "__main__":
    main()