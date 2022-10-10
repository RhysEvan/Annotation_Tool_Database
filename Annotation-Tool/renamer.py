import os
import glob
place = r"C:\Users\Rhys Evans\Universiteit Antwerpen\Master Thesis Autostitching - Documenten\General\Skin_Database"
filenames = glob.glob(place + r'/*')

#to_displace = "cut_labeled"
#to_displace_with = "labeled"
os.chdir(place)
for i, fn in enumerate(filenames):
    os.rename(filenames[i], fn.replace(fn, "synth_skin_"+str(i)+".jpg"))
    
