from PIL import Image
import random

im = Image.open('Area.png')
rgb_im  = im.convert("RGB")         # RGB matrix

count_in = 0
count_pun = 0
count = 0

while(count <= 50000):
    
    x = random.randint(0,800)
    y = random.randint(0,900)
    z = 0
    
    r,g,b = rgb_im.getpixel((x,y))
    
    if(r == 60):
        count_in += 1
        count += 1
        
    else:
        if(r == 80):
            count_pun += 1
            count += 1
            
area_pun = (count_pun / count_in) * 3287263
print(area_pun)