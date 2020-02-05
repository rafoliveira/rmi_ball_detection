import cv2
import os
import sys

image_folder = 'balls_dataset_better'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

    i = images.index(image)
    sys.stdout.write("\r"+str(int((i/len(images))*100))+"%")
    sys.stdout.flush()

cv2.destroyAllWindows()
video.release()