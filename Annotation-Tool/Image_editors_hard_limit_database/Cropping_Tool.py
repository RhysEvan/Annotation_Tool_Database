import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import tqdm.contrib as tqdmc
import cv2

#######################################################################
show = False #gwn aan of uit zetten, aan is showen uit is bijknippen
place = r"C:\Users\Rhys Evans\Universiteit Antwerpen\Master Thesis Autostitching - Documenten\General\Skin_Database"
########################################################################

def make_new_directory(fn, names):
    try:
        os.makedirs(place + r'/database_cut')
    except Exception as e:
        print("folder already exists")
    print("Copying to new folder:")
    for i,name in tqdmc.tenumerate(fn):
        img = cv2.imread(fn[i])
        os.chdir(place + r'/database_cut/')
        cv2.imwrite(names[i],img)

filenames = glob.glob(place + r'/*jpg')
filenames = [fn for fn in filenames if fn.find("cropped")==-1]

if show != True:
    names = os.listdir(place)
    try:
        names.remove('database_cut')
    except Exception as e:
        print("no pre existing databse")
    make_new_directory(filenames, names) #makes new directory with all the images

    print("\nCropping images:")
    for i, fn in tqdmc.tenumerate(filenames):
        try:
            img = cv2.imread(fn) #load in the image
            img = img[236:3236,70:4570] #cut the image
            fn_new = place + r'/database_cut/' + names[i]
            cv2.imwrite(names[i],img)
            old_name = fn_new
            new_name = fn_new.replace("_skin", "_cropped_skin")
            os.rename(old_name, new_name) #to rename the images
        except Exception as e:
            print(f"\n{fn} is fout gegaan \nDe fout is: {e}")


if show == True:
    print("Going to show all images until you type stop")
    filenames = glob.glob(place + r'/*jpg')
    i = 0
    while i != len(filenames):
        img = cv2.imread(filenames[i])
        plt.imshow(img)
        plt.show()
        i += 1