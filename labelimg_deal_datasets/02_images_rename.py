import os


path = "D:\pycharm_project\eg01\水面垃圾"
filelist = os.listdir(path)
count=0
for file in filelist:
    print(file)
for file in filelist:
    Olddir=os.path.join(path,file)
    if os.path.isdir(Olddir):
        continue
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    Newdir=os.path.join(path,str(count).zfill(6)+filetype)
    os.rename(Olddir,Newdir)
    count+=1
