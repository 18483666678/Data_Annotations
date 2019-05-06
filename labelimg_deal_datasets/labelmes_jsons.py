import os
path = 'D:\pycharm_projects\VOC2019\Jepg/'  # path是你存放json的路径
json_file = os.listdir(path)
for file in json_file:
    os.system("python D:\Anaconda3\envs\labelme\Scripts\labelme_json_to_dataset.exe %s"%(path + file))
