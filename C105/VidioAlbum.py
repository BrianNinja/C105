import cv2
import os 

path = "Images/"

images = []
for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','jiji']:
        file_name = path + "/" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)
        
frame = cv2.imread(images[0])

height,width,Channels = frame.shape

size = (width,height)
print(size)



out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0,count-1):
    print((images[i]))
    frame = cv2.imread(images[i])
    out.write(frame)
    


out.release()    
print()