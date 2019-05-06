import cv2
import os



#从视频读取帧保存为图片

# cap = cv2.VideoCapture("D:\迅雷下载/s0506711wz5.p712.1.mp4")
# c=0
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     cv2.imwrite('D:\googledownload\labelme-master\image/'+str(c) + '.jpg',frame) #存储为图像
#     c=c+1
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


path = 'D:\原始图片数据\视频/'
c = 1
for i in os.listdir(path):
    print('视频：%s转换图片'%(path + i))
    cap=cv2.VideoCapture(path+i)
    print('start')

    if cap.isOpened():
        rval,frame=cap.read()
    else:
        rval=False

    timeF = 4  # 跳帧
    while rval:
        rval,frame=cap.read()
        if c % timeF == 0:
            cv2.imwrite('D:\googledownload\labelme-master\image2/'+str(c)+'.jpg',frame)
        c=c+1
        cv2.waitKey(1)
        print(c)
    print('end：保存图片%i张'%c)
    cap.release()