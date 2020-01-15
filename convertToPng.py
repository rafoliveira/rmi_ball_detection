import cv2
import numpy as np
import h5py
import sys
import os
f = h5py.File('b-alls-2019.hdf5', 'r')

def create_images(img, data_type):
	c=0
	print("Creating "+data_type)

	if not os.path.exists(data_type):
		os.makedirs(data_type)

	for i in img:
		data = np.array(i[:,:,:])
		file = data_type + '/ball'+str(c)+'.jpg'
		cv2.imwrite(file, data)
		c+=1
		sys.stdout.write("\r"+str(int((c/len(img))*100))+"%")
		sys.stdout.flush()
	print("\nFinished\n")

create_images(f['negatives']['data'], 'no_balls_dataset')
create_images(f['positives']['data'], 'balls_dataset')
