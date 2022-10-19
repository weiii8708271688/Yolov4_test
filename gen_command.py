import cv2
import pickle
import os
from os import listdir, getcwd
from os.path import join

img_path = "C:/Users/user/Desktop/public/"
lst_img = list(listdir('C:/Users/user/Desktop/public'))
data_path = "C:/Users/user/Desktop/Drown/cfg/obj.data"
cfg_path = r"C:\Users\user\Desktop\Drown\cfg\yolov4.cfg"
weight_path = r"C:\Users\user\Desktop\Drown\cfg\weights\yolov4_last.weights"
output_path = "C:/Users/user/Desktop/Drown/output/output.json"
python_path = "C:/Users/user/Desktop/Drown/json_to_T-brain.py"
PATH = 'darknet detector test ' + data_path + ' ' + cfg_path + ' ' + weight_path

to_be_write = []
for i in lst_img:
    to_be_write.append(PATH + ' ' + img_path + i + ' -dont_show -out ' + output_path + ' -thresh 0.25' + '\n')
    to_be_write.append('python ' + python_path + '\n')


with open('C:/Users/user/Desktop/Drown/cmd_lines.txt', 'w') as f:
    for i in to_be_write:
        f.write(i)

print('done')