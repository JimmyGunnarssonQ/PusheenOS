from PIL import Image 
imag = Image.open("Pusheen.jpg")
for i in range(30):
    imag.save(str(i) + ".jpg")