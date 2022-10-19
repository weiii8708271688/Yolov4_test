import cv2
import pickle
import os
from os import listdir, getcwd
from os.path import join
import pandas as pd



labelFile_path = "C:/Users/user/Desktop/Drown/output/"
lst_txt = listdir(labelFile_path)
print(lst_txt)
to_be_write = []
for i in lst_txt:
    if(i == 'output.json'):
        continue
    with open(labelFile_path + i, 'r') as f:
        to_be_write.append(f.read())

with open('C:/Users/user/Desktop/Drown/' + 'up_load' + '.csv', 'w') as f:
    for i in to_be_write:
        f.write(i)



print('done')