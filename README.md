# Video_processing
* It contains the code for using semi supervised approach for annotating instances for videos using state of the art video object segmentation methods.
* Given a large number of frames for a particular video, it firsts cluster them.
* Then SOTA methods such as STM are used to annotate those clusters along with various manipulation techniques.
* Here the code is provided along with the STM model which is taken from the official STM repository.

# Requirements
Anaconda can be installed for package management .
Then create an environment with:
```javascript
conda create -n myenv
source activate myenv
```
Now after entering the environment install the following packages. 

* Python
* torch
* PIL
* matplotlib
* torchvision
* skimage
* imageio

# Running the code
First run the code to create the directory structure.
```javascript
python create_common_directories.py
```
Then run the clustering code for the complete genre. The genre can contain any number of videos.
```javascript
python complete_generator_cluster_generator.py
```
Then run the second pass clustering code for some more clustering.
```javascript
python pass_2.py

```
Afte generating the final clusters annotate the first frame in each cluster as these are semi supervised methods.
Now final clusters have been generated so after this run:
```javascript
python directory_structure.py

```

This generates masks for a particular video to which path has been specified.
This is for instance wise segmentation so color each new instance with a different color and color of a particular instance must be same across all the shots.
Here is the glimpse for some of the frames of a musical video having singer as the instance.
![Propagated Masks](https://github.com/nishant34/Video_processing/blob/main/Screenshot%20(680).png)




