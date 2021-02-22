from PIL import Image,ImageEnhance,ImageFilter
import os
img1=Image.open("picture.jpg")
img1.save("picture.png") 
img1.show()

try:    
 img1 = img1.rotate(180) 
 img1.save("rotated_picture.jpg") 
except IOError: 
 pass

width, height = img.size 
img1 = img1.resize((width/2, height/2)) 
img1.save("resized_picture.jpg")

img2 = Image.open("picture2.jpg")  
img1.paste(img2, (50, 50)) 
img1.save("pasted_picture.jpg") 

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

print(img1.split())

transposed_img = img1.transpose(Image.FLIP_LEFT_RIGHT) 
transposed_img.save("transposed.jpg") 

        
        
        
        


