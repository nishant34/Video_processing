import os
from path_infos import *

os.mkdir(os.path.join(root_directory,'Annotations'))
os.mkdir(os.path.join(root_directory,'JPEGImages'))
os.mkdir(os.path.join(root_directory,'ImageSets'))
path_1 = os.path.join(root_directory,'Annotations')
path_2 = os.path.join(root_directory,'JPEGImages')
path_3 = os.path.join(root_directory,'ImageSets')
os.mkdir(os.path.join(path_1,'480p'))
os.mkdir(os.path.join(path_2,'480p'))
os.mkdir(os.path.join(path_1,'480p',txt_file_name))
os.mkdir(os.path.join(path_2,'480p',txt_file_name))
os.mkdir(os.path.join(path_3,'2017'))
path_4 = os.path.join(path_3,'2017')
txt_file = open(path_4+'/'+'val1.txt','w')
txt_file.write(txt_file_name)