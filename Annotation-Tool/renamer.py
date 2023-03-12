import os
import glob
place = r"C:\Users\mheva\OneDrive\Bureaublad\temp"
filenames = glob.glob(place + r'/*')

to_displace = "_.tif"
to_displace_with = ".tif"
os.chdir(place)
for i, fn in enumerate(filenames):
    os.rename(filenames[i], fn.replace(to_displace, to_displace_with))
    
