from PIL import ImageFont, ImageDraw, Image  
import numpy as np 
import cv2
import random

#use a truetype font 
font = ImageFont.truetype("Helvetica-Bold.otf", 85)

#range= no. of plates we want to generate
for r in range(1):
    number_plate_1 = "   F BC0" + str(random.randint(100, 999))
    #plate on which the number must be printed
    img = cv2.imread("flag.jpg")

    pil_img = Image.fromarray(img)
    draw = ImageDraw.Draw(pil_img)
    draw.text((25, 30), number_plate_1, 256, font=font)

    # draw.text((15, 130), number_plate_2, font=font)
    cv2_img = cv2.resize(np.array(pil_img), (535, 160))
    # cv2_img = cv2.bitwise_not(cv2_img)
    # cv2.imshow("number_plate", cv2_img)
    cv2.imwrite(number_plate_1 + ".png", cv2_img)
    # cv2.waitKey(10)

cv2.destroyAllWindows()
