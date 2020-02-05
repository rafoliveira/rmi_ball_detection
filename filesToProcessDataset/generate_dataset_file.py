import os

path='data/obj/'

all_files=os.listdir('/data/obj/')

imgList= [f for f in all_files if 'jpg' in f]

print(imgList)

textFile=open('train.txt','w')


for img in imgList:
    imgPath=path + img +'\n'
    textFile.write(imgPath)
