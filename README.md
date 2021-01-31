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
First run the clustering code.
```javascript
python pass_1.py

```
And then to see the tensorboard results, in the  command line:
```javascript
python -m tensorboard.main --logdir=[PATH_TO_LOGDIR]
```


