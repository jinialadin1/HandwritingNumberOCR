# Pillow package
from PIL import Image
import os
import image_process

data_path = "../origin/"
save_sum_path = "./sum/"
save_div_path = "./divided/"
'''
def search(dirname, ext):
    count = 0
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        findext = os.path.splitext(full_filename)[-1]
        if findext == ext:
            count += 1
    return count

file_count = search(os.getcwd()+'/'+data_path,'jpg')
'''
for i in range(0,64):
    path = data_path+'data'+str(i)+'.jpg'
    
    im = Image.open(path)
        
    #find the start point of crop
    crop_corner = image_process.FindCorner(path)
    crop_corner[0] += 10
    crop_corner[1] += 10

    #crop image size
    crop_d = (165,260)
    crop_line_d = (16,25)
    
    crop_start = [crop_corner[0], crop_corner[1]]
    
    for number in range(0,10):
        crop_start[0] = int(round(crop_corner[0]+number*1.5))
        for rpt in range(0, 10):
            cropImage = im.crop((crop_start[0], crop_start[1], crop_start[0]+crop_d[0], crop_start[1]+crop_d[1]))

            cropImage.save(save_sum_path+str(number)+'_'+str(rpt)+'_'+str(i)+".jpg")
            cropImage.save(save_div_path+'/'+str(number)+'/'+str(number)+'_'+str(rpt)+'_'+str(i)+".jpg")

            crop_start[0] += crop_d[0]+crop_line_d[0]
        
        crop_start[1] += crop_d[1]+crop_line_d[1]
