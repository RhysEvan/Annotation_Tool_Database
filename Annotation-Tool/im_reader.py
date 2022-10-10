from skimage import io
import matplotlib.pyplot as plt
import os
place = r"C:\Users\Rhys Evans\Universiteit Antwerpen\Master Thesis Autostitching - Documenten\General\Skin_Database"
os.chdir(place)
im = io.imread("synth_skin_0_label.tif")
plt.imshow(im)
plt.show()