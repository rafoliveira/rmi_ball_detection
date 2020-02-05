import os
import sys
import cv2
import numpy as np 

def better_quality(data_type, name):
	img = cv2.imread(data_type + '/' + name, cv2.IMREAD_UNCHANGED)
	 

	scale_percent = 2400 # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
	 
	kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	dst = cv2.filter2D(resized, -1, kernel)

	if not os.path.exists(data_type + '_better'):
		os.makedirs(data_type + '_better')

	cv2.imwrite(data_type + '_better/' + name, resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def iteration(data_type):	
	all_balls = os.listdir(data_type)

	print("Creating better quality images, " +data_type)
	for b in all_balls:
		better_quality(data_type, b)

		i = all_balls.index(b)
		sys.stdout.write("\r"+str(int((i/len(all_balls))*100))+"%")
		sys.stdout.flush()
    
	print("\n" +data_type+ " finished\n")


#iteration('no_balls_dataset')
iteration('balls_dataset')
