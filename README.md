
## About
This pipeline is created to upload 3D manually-segmented CX neuropils, or more generally volumes, onto Catmaid.
The pipeline is broken down into 2 steps:
1) segmenting volumes
2) uploading volumes to catmaid


## Part 1: segmenting the neuropils
## Before starting
Two software are needed for segmentation, **ImageJ/1.54f** and **Amira/5.3.3**.
If you do not have these sotware, refer to online resources on how to install ImageJ and Amira (Note: Amira is not a free software).
ImageJ:
https://imagej.net/software/fiji/downloads
Amira:
https://www.thermofisher.com/se/en/home/electron-microscopy/products/software-em-3d-vis/amira-software.html

## Usage

### ImageJ
Open up Image J.

Upload your image stack on ImageJ, where you are segmenting from, using "File>Import>Image Sequence..."

A window should appear.
On the first line click the "Browse" button and select the folder with your images of interest (ensure only your images are in this folder).
On the "step:" line change it to 10 and on the "Scale" line to 10%.
then click "OK" on the bottom right.

The images will take a while to all load.

Once loaded, export your images by going to "File>Save As>Tiff..."

select where you would like your new image stack (saved under one tiff file) to be saved, name it and click "save". 

Now you can move over to Amira.

### Amira

#### Input & segmentation
Please refer to the brain reconstruction manual below on inputting data into and using Amira to segment. 
https://drive.google.com/drive/folders/1PHDAv1DZ8f6XFOtu5dSZG-CVusRvxKJy?usp=sharing

Note: After opening Amira, correct voxel size in order to have correct dimensions in Catmaid. I.e., for dung beetle CX overview image stack voxel sizes are x,y,z=40,40,50 but increase it by a factor of 10 to 400,400,500 as we downsampled it in ImageJ.
#### exporting
Before exporting, save your Amira project. Then, for every volume within your segmentation save a copy of your Amira Project. In each project remove all volumes except one unique volume to each project. In this way, each export will have only one unique volume (no simpler step currently made)(information on saving and deleting can be found from the link above).

Depending on if you made your volumes solely with Amira or also with Biomedisa, the following steps differ.
##### Solely Amira
skip if Biomedisa was used.
Go to the object pool tab and click on your label object.
A Isosurface button will appear (above right in your window), click on it.
Next, a new Isosurface object will appear, click on it and below in the properties window click the green Apply button. This may take some time.

Go to your Isosurface object a SurfaceGen object will appear (above right in your window), click on it. Next, a new surfaceGen object will appear, click on it and below in the properties window click the green Apply button. This may take some time.

##### Biomedisa
Go to the object pool tab and click on your label object.
A surfaceGen button will appear (above right in your window), click on it.
Next, a new surfaceGen object will appear, click on it and below in the properties window click the green Apply button. This may take some time.

#### exporting (cont.)
Then, a new object should be created with the same name as your label but finishing with .surf. Click on the new object and at the top a button called SurfaceView should appear. Click on it to see what your surface object looks like. It is likely the surface object will be too large to export so beside Simplify in the properties window reduce the number of faces by a factor of 10 (remove a zero). Click perserve slice structure checkmark and click Simplify now (simplyfing should be seen by a a reduction of faces on your surface object in the viewer). Once simplified you can now export.

Right click on the surface object and click Save Data As...
Choose where you would like the object to be saved and the name and make sure to change the file format to STL ascii (.stl).

Repeat these steps for all volumes of interest.

## Part 2: uploading neuropils to catmaid
## Before starting

A **Catmaid account** is needed for this code.

Before downloading this repository it should be stated that without a Catmaid account following the instructions below becomes obsolete.

This code is run on the terminal.
## Installation
This program can be directly installed from github (green Code button, top right).

Make sure to change into the downloaded directory, the code should resemble something like this.

```bash=
cd Downloads/upload_volume
```

### Conda environment
First make sure conda is installed. If you do not have conda, refer to online resources on how to install conda.
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

Once installed, we can make a conda environment.

```bash=
conda create --name pymaid
#activate
conda activate pymaid
```

### Python version
The python version for running this script is python=3.6
```bash=
conda install python=3.6
```

### Dependencies
The script runs with pip\==21.3.1 and python-catmaid==2.0.4

Update your dependencies, if you do not already have the versions for these dependencies.

```bash=
pip install --upgrade pip==21.3.1 wheel==0.37.1 setuptools==59.6.0

pip install python-catmaid==2.0.4 -U
```

### Make environmental variables

The environmental variables are the login credentials required to access catmaid online. Which include, the catmaid server, and your API token (the API token replaces your username and password to the server). Your API token can be found following the instructions on this website:
https://catmaid.readthedocs.io/en/stable/api.html#api-token

There are two ways to access catmaid online. The deemed safer version will be covered here, for the other option refer to this link:
https://pymaid.readthedocs.io/en/latest/source/intro.html

Add your new environmental variables via the bash_profile file.

```bash=
nano ~/.bash_profile
```
When in nano, add the following lines to your code, with  respect to your account. 
```bash=
export CATMAID_SERVER='https://www.your.catmaid-server.org'
export CATMAID_API_TOKEN='your_token'
```
Don't forget to source.
```bash=
source ~/.bash_profile
```
Verify after sourcing that you are still in your pymaid conda environment.
The script should be all ready to run.

## Usage
### Input
#change permissions in catmaid
The code can be run as follows (most arguments are optional, see below).
```bash=
   python upload_volume.py [-h] [-v] -p PROJECT_ID -i INPUTFILE [-n NAME]
                        [-r RESIZE] [-s]
```
The help page can be accessed with the -h or --help flag
```bash=
python plot_pymaid.py -h
python plot_pymaid.py --help
```
The program version can be accessed with the -v or --version flag
```bash=
python plot_pymaid.py -v
python plot_pymaid.py --version
```
There are two required arguments for running this program, PROJECT_ID and INPUTFILE. PROJECT_ID specifies which species stack you are uploading your volume to. INPUTFILE is the volume file of interest to uplaod.
```bash=
python plot_pymaid.py -p PROJECT_ID -i example_input.stl
```

The following arguments are optional.

NAME, name on catmaid for volume.
```bash=
python plot_pymaid.py -p PROJECT_ID -i example_input.stl -n example_name
```
RESIZE, specificed resize factor (i.e., input 10, 10 times larger).
```bash=
python plot_pymaid.py -p PROJECT_ID -i example_input.stl -r
```
Finally, -s, to show the volume before upload.
```bash=
python plot_pymaid.py -p PROJECT_ID -i example_input.stl -s
```

### Example inputs

If you would like to upload to the the "galenus" project the CX volume. 
```bash=
python3 plot_pymaid.py -p 15 -i input/galenus_CX.stl 
```

If you would like to upload to the the "galenus" project the CX volume, name it CX, resize it by a factor of 10 and show it before upload. 
```bash=
python3 plot_pymaid.py -p 15 -i input/galenus_CX.stl -n CX -r 10 -s
```
