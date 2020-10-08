import os
from PIL import Image
final_dir = 'RGMP/DAVIS/Annotations/480p/data_nishant'
save_path = os.path.join(final_dir,'00000.png')
#a = Image.open('Segmentation_export_s34.png')
a = Image.open('00000.png')
b = a.resize((910,480),Image.ANTIALIAS)
b.save(save_path)