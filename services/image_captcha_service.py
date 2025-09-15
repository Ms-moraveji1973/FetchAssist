import os
import pytesseract
from natsort import natsorted
from PIL import Image
import cv2
import requests
def image_processing(image:str):
    # ---- read image from Image module ----

    instance = Image.open(image)
    alpha_number = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # ---- clean noise from background ----
    def remove_noise():
        threshold = 180
        print(threshold)
        img = instance.convert('RGB')
        pixel_access = img.load()
    
        for j in range(img.size[1]):
            for i in range(img.size[0]):
                if (pixel_access[i, j][0] > threshold) \
                        and (pixel_access[i, j][1] > threshold) \
                        and (pixel_access[i, j][2] > threshold):
                    pixel_access[i, j] = (255, 255, 255)
                else:
                    pixel_access[i, j] = (0, 0, 0)
        separate_number(img)
    
    
    # separate the number from each other
    def separate_number(image):
        image_pixel_access = image.load()
        width , height = image.size
        start_x_loc = None
        in_character = False
        image_list = []
    
        for x in range(width):
            is_column = any(image_pixel_access[x,y] == (0,0,0) for y in range(height))
            if is_column and not in_character:
                in_character = True
                start_x_loc = x
            elif not is_column  and in_character :
                in_character = False
                bbox = (start_x_loc-1,0,x,height)
                crop_image = image.crop(bbox)
                image_list.append(crop_image)
    
        for i,crop in enumerate(image_list) :
            crop.save(f"images/numbers/number_{i+1}.png")
    remove_noise()
    
    alpha_list = []
    result = ""
    dire = "/Users/mohammads/Projects/simple_CAPTCHA_solver/images/numbers/"
    final_image = natsorted(os.listdir(dire))
    
    # save image in disk
    
    for i in final_image:
            img = cv2.imread(dire + "/" + i)
    
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
            custom_config = r'--oem 3 --psm 10 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
            text = pytesseract.image_to_string(binary_img, config=custom_config).strip()
            alpha_list.append(text)
            print(alpha_list)
    
    
    # delete image from disk
    for i in final_image:
        os.remove(dire+"/"+i)
    
    result += "".join(alpha_list)
    print("This is your captcha character :",result)
    return result
