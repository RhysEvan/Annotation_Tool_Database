import os
import glob
import numpy as np
import cv2
place = r"C:\Users\mheva\OneDrive\Bureaublad\database_cadaver"
filenames = glob.glob(place + r'/*')
os.chdir(place)
sz_out = (500,500)
for i, name in enumerate(filenames):
    im = cv2.imread(name)
    im = cv2.resize(im, tuple(sz_out))
    im = cv2.imwrite(name, im)
