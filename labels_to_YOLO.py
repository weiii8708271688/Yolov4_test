import cv2
import pickle
import os
from os import listdir, getcwd
from os.path import join



wd = getcwd()
lst_img = list(listdir(wd+'\\Images'))
lst_txt = list(listdir(wd+'\\Labels'))

for i in range(len(lst_img)):
    img_wd = wd + '\\Images\\' + lst_img[i]#圖片的路徑
    txt_wd = wd + '\\Labels\\' + lst_txt[i]#T-brain txt的路徑
    dest_wd = wd + '\\Yolos\\' + lst_txt[i]#最後儲存要訓練檔案的路徑
    
    img = cv2.imread(img_wd, 1)
    Y = len(img)#幾乘幾 1920*1080 (Y*X)
    X = len(img[0])#幾乘幾 1920*1080 (Y*X)
    to_be_write = []
    with open(txt_wd, 'r') as f:#先讀檔 把T-brain的格式轉成yolo吃的格式
        data = f.read()
        data = list(data.split('\n'))
        to_be_write = []
        for row in data:
            if(len(row) == 0):
                continue
            row = row.split(',')
            Class = row[0]
            x = (float(row[1]))
            y = (float(row[2]))
            w = (float(row[3]))
            h = (float(row[4]))

            x = (x+w/2)/X
            y = (y+h/2)/Y
            w = w/X
            h = h/Y

            to_be_write.append(Class + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')
    with open(dest_wd, 'w') as f:#再寫檔
        for words in to_be_write:
            f.write(words)

    #print(lst_img[i] +  'done')
print('All done')


        