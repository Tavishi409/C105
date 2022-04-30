import os 
import cv2
path = "Images/"
images =[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        #example filename for the first file could be images/110.jpg
        file_name = path+"/"+file

        print(file_name)
         #add file names one by one into the images array      
        images.append(file_name)

count=len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width, height)
print(size)

out=cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'MP4V'),5,size)

for i in range(0, count-1):
    print(images[i])
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()