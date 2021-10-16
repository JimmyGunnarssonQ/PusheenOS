from PIL import Image 
imag = Image.open("Pusheen.jpg")
i=0
while True:
    imag.save("Pusheen" + str(i) + ".jpg")
    i+=1