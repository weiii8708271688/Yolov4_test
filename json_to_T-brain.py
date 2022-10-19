import cv2
import pickle
import os
from os import listdir, getcwd
from os.path import join
import json


with open(r'C:\Users\user\Desktop\Drown\output\output.json') as f:
    data = json.load(f)

img_path = "C:/Users/user/Desktop/public/"
name = list(data[0]['filename'].split('/'))[-1][0:7]
img = cv2.imread(img_path+name+'.png', 1)
Y = len(img)#幾乘幾 1920*1080 (Y*X)
X = len(img[0])#幾乘幾 1920*1080 (Y*X)
to_be_write = []
for i in data[0]['objects']:
    temp = []
    class_id = str(i['class_id'])
    coordinate = i['relative_coordinates']
    center_x = float(coordinate['center_x'])*X
    center_y = float(coordinate['center_y'])*Y
    w = float(coordinate['width'])*X
    h = float(coordinate['height'])*Y
    x = center_x - w/2
    y = center_y - h/2
    if(x < 0):
        x = 0
    if(y < 0):
        y = 0
    to_be_write.append(name + ',' + class_id + ',' + str(int(x)) + ',' + str(int(y)) + ',' + str(int(w)) + ',' + str(int(h)) + '\n')





with open('C:/Users/user/Desktop/Drown/output/' + name + '.csv', 'w') as f:
    for i in to_be_write:
        f.write(i)

print(name + '.csv' + ' done!')