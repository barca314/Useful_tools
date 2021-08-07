import os
import pandas as pd
import cv2

#遍历文件夹内所有文件的函数
def getFileList(dir,Filelist, ext=None):

    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
    
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, Filelist, ext)
 
    return Filelist
#定义需要遍历的文件夹的名字
imglist = getFileList('./', [], 'jpg')
print('本次执行检索到 '+str(len(imglist))+' 张图像\n')

index = 0

for imgpath in imglist:
    #print(imgpath)
    index = index + 1
    file_name = os.path.splitext(os.path.basename(imgpath))[0]+'.jpg'
    #print(file_name)
    print(str(index/len(imglist)*100)+'%')
    image = cv2.imread(file_name)
    #cv2.imshow('test',image)
    weight = image.shape[1]
    height = image.shape[0]

    resize_scale = (640, int(640/weight*height))
    resized_img = cv2.resize(image,resize_scale)
    #cv2.imshow('resized',resized_img)
    cv2.imwrite('./resized/'+file_name,resized_img)
    #cv2.waitKey(0)
    #print(image.shape)
print('done')