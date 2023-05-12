import os
import imageio

file_dir = sorted(os.listdir('gif_maker/images'))
print(file_dir)

IMAGES= []

for file_name in file_dir:
    image = imageio.imread('gif_maker/images/'+file_name)
    IMAGES.append(image)

#mimsave function: convert list of image to gif
imageio.mimsave('gif_maker/output.gif',IMAGES)
