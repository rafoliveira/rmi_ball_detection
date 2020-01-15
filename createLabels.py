import os
import h5py
import sys
f = h5py.File('b-alls-2019.hdf5', 'r')

def create_labels(img, data_type):
    
    print("Creating "+data_type+" labels")
    
    if not os.path.exists(data_type + '_labels'):
        os.makedirs(data_type + '_labels')
    
    for i in range(len(img)):
        
        f= open(data_type + '_labels/ball' + str(i) + '.txt',"w+")
        f.write("1 " +str(img[i][1]/32)+ " " +str(img[i][2]/32)+ " " +str(2*img[i][3]/32)+ " " +str(2*img[i][3]/32))
        f.close()
        

        sys.stdout.write("\r"+str(int((i/len(img))*100))+"%")
        sys.stdout.flush()
    print("\nFinished\n")
        
#create_labels(f['negatives']['labels'], 'no_balls_dataset')
create_labels(f['positives']['labels'], 'balls_dataset')
