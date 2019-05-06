import os
from PIL import Image


# 写入cv2mask文件图片
path = r'D:\googledownload\Mask_RCNN-master\train_data\labelme_json/'
image_dir = r'D:\googledownload\Mask_RCNN-master\train_data\cv2_mask/'
for i in os.listdir(path):
    print(i)
    a = []
    for j in os.listdir(path+i):
        print(j)
        a.append(j)

    print(a[2])
    if a[2] == 'label.png':
        img = os.path.join(path+i+'/'+a[2])
        print(img)
        # exit()
        with Image.open(img) as f:
            crop = f.copy()
            crop.save(os.path.join(image_dir,'{0}.png'.format(i.split('_')[0])))



# 重命名
# image_dir = r'D:\googledownload\Mask_RCNN-master\train_data\cv2_mask/'
#
# for i in os.listdir(image_dir):
#     print(i)
#     a = i.split('_')[0]
#     print(a)
#     exit()