import os 
import shutil
from shutil import copyfile
import subprocess
import Shot_inference
from PIL import Image
import trial
from path_infos import *
step_size = 24

mask_count = 0  
mask_names = []
trial.initial_clearance()
os.chdir(current_dir)
for mask_name in os.listdir(root_mask_path):
    mask_names.append(mask_name)
with open(initial_path+'shot.txt') as f:
    array = []
    count =  0
    for line in f: # read the shots
        array.append([int(x) for x in line.split()])
        #initial approach
        #creating a directory structure
        #print(array[count][0])
        #os.mkdir(os.path.join('shots',str(count)))
        #curr_path = os.path.join('shots',str(count))
        #adjust names accordingly
        mask_no = format(count,'03d')
        #curr_mask = root_mask_path + 'Segmentation_export_s' + str(mask_no) + '.png'
        curr_mask = root_mask_path + mask_names[count]
        #shutil.copy(curr_mask,common_mask_path+'00000.png')
        #resizing
        a = Image.open(curr_mask)
        b = a.resize((910,480),Image.ANTIALIAS)
        b.save(common_mask_path+'00000.png')
        j = 0
        global_indices = []
        for i in range(array[count][0],array[count][1]+1,step_size):
            print(array[count][0])
            print(array[count][1])
            image_no = format(i+1,'05d')
            global_indices.append(i+1)
            curr_image = root_path+'/image_' + str(image_no) + '.png'
            fj = format(j,'05d')
            try:
             #shutil.copy(curr_image,curr_path)
             #shutil.copy(curr_image,common_image_path+str(fj)+'.jpg')
             #resize
             c = Image.open(curr_image)
             d = c.resize((910,480),Image.ANTIALIAS)
             d.save(common_image_path+str(fj)+'.jpg')
             j+=1
             
            except OSError:
                print('1st_pass')
                pass
        print("execution begins")
        #exec(open('Shot_inference.py').read())
        Shot_inference.execute_fn()
        #subprocess.call("Shot_inference.py",shell=True)
        print("execution over")
        #subprocess.call(['eval_DAVIS.py', '-g','1','-s','val1','-y','17'])
        #deleting contents of the common folder 
        #for filename in os.listdir(common_image_path):
         #   file_path = os.path.join(common_image_path,filename)
           # try:
            #    shutil.rmtree(file_path)
            #except OSError:
               # print('2nd_pass')
             #   pass
        #for filename in os.listdir(common_mask_path):
         #   file_path = os.path.join(common_mask_path,filename)
          #  try:
           #     shutil.rmtree(file_path)
            #except OSError:
                #print('second_last_pass')
            #    pass
        #new method of deleting
        #try:
         #os.system('rmdir /S /Q "{}"'.format(common_image_dir))
         #os.system('rmdir /S /Q "{}"'.format(common_mask_dir))
         #os.mkdir(common_image_dir)
         #os.mkdir(common_mask_dir)
        os.chdir(common_image_dir)
         #os.chdir(common_mask_dir)
        for filename in os.listdir(common_image_dir):
          file_path = os.path.join(common_image_dir,filename)
          try:
              os.remove(file_path)   

          except OSError:
            print('nahi ho rha')
            pass 
        os.chdir(common_mask_dir)
        for file_name in os.listdir(common_mask_dir):
            file_path = os.path.join(common_mask_dir,file_name)
            try:
                os.remove(file_path)
            except OSError:
                print('nahi ho rha')    

        os.chdir(current_dir) 
        #copying results into final mask folder
        global_count_helper = 0
        for filename in os.listdir(common_results_path):
            file_path = os.path.join(common_results_path,filename)
            #f_mask_count  = format(mask_count,'05d')
            #global_index
            f_mask_count = format(global_indices[global_count_helper],'05d')
            global_count_helper+=1
            dst = final_mask_path + f_mask_count+'.png'
            #os.rename(filename,dst)
            #os.rename(file_path,dst)
            #shutil.move(file_path,dst)
            #resize
            r = Image.open(file_path)
            s = r.resize((1280,720),Image.ANTIALIAS)
            s.save(dst)
            mask_count+=1
        #deleting files from common results path
        os.chdir(common_results_dir)
        for filename in os.listdir(common_results_dir):
            file_path = os.path.join(common_results_dir,filename)
            try:
                os.remove(file_path)

            except OSError:
                print('nahi ho rhaaaaaa')  
        os.chdir(current_dir)              
        #for filename in os.listdir(common_results_path):
         #   file_path = os.path.join(common_results_path,filename)
          #  try:
           #     shutil.rmtree(file_path)
            #except OSError:
             #   print('last_pass')
              #  pass       
            


        
        
        count+=1

        
        


     