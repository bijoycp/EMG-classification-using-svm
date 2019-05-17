import csv
import os
import sys 

path='data_txt'
path_tar='data_csv'
print("start")

for(direcpath,direcnames,files) in os.walk(path):
    for file in files:
        print(files)
        # label=label_img(dirname)
        path1 =path+'/'+file
        with open(path1 , 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)
            print(lines)
            path1 =path_tar+'/'+file+".csv"
            with open(path1, 'w') as out_file:
                writer = csv.writer(out_file)                
                writer.writerows(lines)