from PIL import Image,ImageEnhance,ImageFilter
import os
img1=Image.open("shrutii.jpg")
img1.save("shrutii.png") 
img1.show()
 #to change the dimension
MAX_SIZE=(250,250)
img1.thumbnail(MAX_SIZE)
img1.save("shruti2.jpg")
for item in os.listdir():    # for large no. of images havinng same process
    if item.endswith(".jpg"):
        img1=Image.open(item)
        filename,extension=os.path.splitext(item)
        img1.save(f"{filename}.png")
Enhancer=ImageEnhance.Sharpness(img1)
Enhancer.enhance(5).save("shru.jpg")
enhancer=ImageEnhance.Color(img1)
enhancer.enhance(0).save("shrut.jpg")
enhancer.enhance(3).save("sh.jpg")
enhancers=ImageEnhance.Brightness(img1)
enhancers.enhance(3).save("ss.jpg")
enhancerk=ImageEnhance.Contrast(img1)
enhancerk.enhance(4).save("sk.jpg")
img1.filter(ImageFilter.GaussianBlur(radius=4)).save("skd.jpg")  #by default radius is 2  
        
        
        
        


