import os
import glob
place = r"C:\Users\mheva\OneDrive\Bureaublad\fotos rhys"
filenames = glob.glob(place + r'/*')
to_displace = "JPG"
to_displace_with = "jpg"
os.chdir(place)
for i, fn in enumerate(filenames):
    os.rename(filenames[i], fn.replace(to_displace, to_displace_with))
    
