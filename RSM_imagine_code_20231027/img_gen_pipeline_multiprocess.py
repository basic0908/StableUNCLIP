import keyboard, sys, os
from clip_image_vector_30 import *
from unclip_50 import *
from unclip_text_variation_51 import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import multiprocessing, threading, cv2


EMBEDS_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\22_image_embeds\00.npy"
OUTPUT_DIR = r"C:\Users\ibara\Downloads\StableUNCLIP\RSM_imagine_dataset_v5\beer\OUTPUT_DIR"
PRED_EMV_LATEST = r"C:\Users\ibara\OneDrive - 株式会社エヌ・ティ・ティ・データ経営研究所\008_NTT人情研\202310TASK\data\RealtimeGeneration\pred_emv_latest.csv"

def replaceImage(output_dir):
    current_image = cv2.imread(os.path.join(output_dir, 'current_image.jpg'))
    next_image = cv2.imread(os.path.join(output_dir, 'next_image.jpg'))
    cv2.imwrite(os.path.join(output_dir, 'current_image.jpg'), next_image)
    cv2.imwrite(os.path.join(output_dir, 'prev_image.jpg'), current_image)

def embedsToImage(pipe, embeds_dir, output_dir):
    embeds = np.load(embeds_dir)

    if not np.isnan(embeds).any():
        # converting embeds to next image
        image = torch.tensor(embeds, dtype=torch.float16).to("cuda")
        image = pipe(image_embeds=image).images[0]

        output_path = os.path.join(output_dir, 'next_image.jpg')
        image.save(output_path)

    else:
        print('---- NOISE ABOVE THRESHOLD ----')


def showImage(output_dir, next_dir, weight):
    img = mpimg.imread(output_dir)
    next_img = mpimg.imread(next_dir)
    
    plt.axis('off')
    plt.imshow(cv2.addWeighted(img, (1-weight), next_img, weight, 0))
    plt.show(block=False)
    plt.pause(0.1)


def toEmbeds(csv_file, embeds_dir):
    arr = np.loadtxt(csv_file, delimiter=",")
    reshaped_arr = arr[-1, :].reshape(1, -1)
    
    np.save(embeds_dir, reshaped_arr)


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
    global EMBEDS_DIR, OUTPUT_DIR, PRED_EMV_LATEST
    
    #model_clip_image_vector_30, processor_clip_image_vector_30, pipe_unclip_50 = load(optional=True)
    pipe_unclip_50 = load()

    
    print("---- INITIALIZING PROCESS ----")
    print("---- END - ESC  PAUSE - P   RESUME - R ----")


    paused = False 

    while True:
   
        if not paused:
            toEmbeds(PRED_EMV_LATEST, EMBEDS_DIR)

    # ----------- MultiProcessing method
            # process = multiprocessing.Process(target=embedsToImage, args=(pipe_unclip_50, EMBEDS_DIR, OUTPUT_DIR))

            # process.start()
            # while process.is_alive():
            #     showImage(os.path.join(OUTPUT_DIR, 'output_image.jpg'))
            # process.join()

    # ----------- No Concurrency method
            # embedsToImage(pipe_unclip_50, EMBEDS_DIR, OUTPUT_DIR)
            # showImage(os.path.join(OUTPUT_DIR, 'output_image.jpg'))

    # ----------- MultiThreading method
            embedsToImageThread = threading.Thread(target=embedsToImage, args=(pipe_unclip_50, EMBEDS_DIR, OUTPUT_DIR))
            embedsToImageThread.start()

            if embedsToImageThread.is_alive():
                # displaying gradual transition
                for i in np.arange(0, 1.1, 0.1):
                    showImage(os.path.join(OUTPUT_DIR, 'prev_image.jpg'), os.path.join(OUTPUT_DIR, 'current_image.jpg'), i)
            
            embedsToImageThread.join()
        
            replaceImage(OUTPUT_DIR)

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