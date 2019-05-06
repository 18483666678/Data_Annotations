import os
import random
from glob import glob
import shutil

labelimg_path = "D:\pycharm_project\eg01\水面垃圾/"
saved_path = "./VOC2007/"

if not os.path.exists(saved_path + "Annotations/"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")


image_files = glob(labelimg_path + "*.jpg")
print("copy image files to VOC007/JPEGImages/")
for image in image_files:
    shutil.copy(image, saved_path + "JPEGImages/")

xml_files = glob(labelimg_path + "*.xml")
print("copy image files to VOC007/Annotations/")
for xml in xml_files:
    shutil.copy(xml, saved_path + "Annotations/")

trainval_percent = 0.66
train_percent = 0.5
xmlfilepath = saved_path + 'Annotations/'
txtsavepath = saved_path + 'ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open(saved_path + 'ImageSets/Main/trainval.txt', 'w')
ftest = open(saved_path + 'ImageSets/Main/test.txt', 'w')
ftrain = open(saved_path + 'ImageSets/Main/train.txt', 'w')
fval = open(saved_path + 'ImageSets/Main/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
             ftrain.write(name)
        else:
             fval.write(name)
    else:
         ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()