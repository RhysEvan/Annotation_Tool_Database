from PIL import Image
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import tqdm.contrib as tqdmc
import cv2

def crop(path, input, height, width):
    k = 0
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            a.load()
            a.save(input.replace(".jpg","_{}_.jpg".format(k)))
            k += 1

def make_new_directory(fn, names):
    try:
        os.makedirs(path + r'/database_chopped')
    except Exception as e:
        print("folder already exists")
    print("Copying to new folder:")
    for i,name in tqdmc.tenumerate(fn):
        img = cv2.imread(fn[i])
        os.chdir(path + r'/database_chopped/')
        cv2.imwrite(names[i],img)

path = r"C:\Users\Rhys Evans\Universiteit Antwerpen\Master Thesis Autostitching - Documenten\General\Skin_Database\database_cut"
filenames = glob.glob(path + r'/*jpg')
filenames = [fn for fn in filenames if fn.find("split")==-1]
names = os.listdir(path)

try:
    names.remove('database_chopped')
except Exception as e:
    print("no pre existing databse")
make_new_directory(filenames, names) #makes new directory with all the images

path = path + r'/database_chopped/'
filenames = glob.glob(path + r'/*jpg')
filenames = [fn for fn in filenames if fn.find("split")==-1]

for i, name in tqdmc.tenumerate(filenames):
    crop(path, filenames[i], 500, 500)

filenames = glob.glob(path + r'/*jpg')
for i, name in tqdmc.tenumerate(filenames):
    fn_new = filenames[i]
    old_name = fn_new
    new_name = fn_new.replace("cropped_skin", "split_skin")
    os.rename(old_name, new_name) #to rename the images

path = path + r'/database_chopped/'
filenames = glob.glob(path + r'/*jpg')
for i, name in tqdmc.tenumerate(filenames):
    if filenames[i].find("_.jpg") == -1:
        os.remove(filenames[i])
    else:
        print("not removing")