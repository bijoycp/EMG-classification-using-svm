import sys
sys.path.append("/home/cp/.virtualenvs/cv/lib/python3.6/site-packages")
import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
#from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import csv 

path='data'
data_len=1500
rows = []
def create_train_data():
    training_data = []
    label=0
    for (dirpath,dirnames,filenames) in os.walk(path):
        for dirname in dirnames:
            print(dirnames)
            for(direcpath,direcnames,files) in os.walk(path+"/"+dirname):
                for file in files:
                    actual_path=path+"/"+dirname+"/"+file
                    print(files)
                    # label=label_img(dirname)
                    path1 =path+"/"+dirname+'/'+file
                    rows = []
                    ii=0
                    with open(path1, 'r') as csvfile: 
                        # creating a csv reader object 
                        csvreader = csv.reader(csvfile)
                        next(csvreader) 
                        
                        for row in csvreader:                                                          
                            
                            if(ii>data_len):
                                break
                            rows.append(int(row[0],10))
                            ii=ii+1

                            # print(label)
                    print(label) 
                    print("**************************")
                    training_data.append([rows,label])
            label=label+1
            print(label)
    shuffle(training_data)
    np.save('train_data.npy', training_data)
    print(training_data)
    return training_data




train_data = create_train_data()
# print(train_data)




