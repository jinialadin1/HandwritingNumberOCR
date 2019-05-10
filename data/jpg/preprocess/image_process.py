#import the necessary packages
from PIL import Image

#find the corner of the number handwriting square
def FindCorner(data_path):
    #load the image
    img = Image.open(data_path)

    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i*width:(i+1)*width] for i in range(height)]
    
    start=[]
    
    #if more than 10 pixels are on the same line
    #define that line as a real line on the paper
    for y in range(400,300,-1):
        for x in range(350,450):
            comp1=pixels[y][x]
            comp2=pixels[y][x+1]
            comp3=pixels[y][x+2]
            if(comp1!=255 and comp2!=255 and comp3!=255):
                count=0
                for i in range(0,20):
                    if(pixels[y][x+i]!=255):
                        count+=1
                if(count>10):
                    start.append([x,y])
                    break
    return start[0]

