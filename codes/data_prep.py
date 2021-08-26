#!/usr/bin/env python
# coding: utf-8

# import all packages
from nilearn.connectome import ConnectivityMeasure
from nilearn.input_data import NiftiLabelsMasker
from load_confounds import Scrubbing
from nilearn import datasets
from os.path import join

import nibabel as nib 
import numpy as np
import shutil
import os

# intialize the layout to retrieve the data
path = '/path/to/fmriprep/' 
file_name = 'task-rest_space-MNI152NLin2009cAsym_desc-preproc_bold'
subjects = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15','16','17', '18']
condition = ['control', 'deaf']
task = 'func'
ext = 'nii.gz'

# variables attribution
conn_measure = ConnectivityMeasure(kind='correlation', vectorize=True, discard_diagonal=True)              
all_features = {'condition':[], 'subject':[], 'connectomes':[]} # where all the features are stored
schaefer_atlas = datasets.fetch_atlas_schaefer_2018(n_rois=100) # load the atlas 
files_nii = []

for sub in subjects:
    
    for cond in condition:
        filename = f'sub-{cond}{sub}/{task}/sub-{cond}{sub}_{file_name}.{ext}'
        sub_func = os.path.join(path, filename)
        # print (sub_func) to keep track of the loop

        if os.path.isfile(sub_func): # verify if path exist 
            img_load = nib.load(sub_func)
            files_nii=np.append(files_nii, img_load)
        
            confounds = Scrubbing().load(sub_func)

            # initialize the masker
            masker = NiftiLabelsMasker(labels_img=schaefer_atlas.maps, t_r=2.2, standardize=True,
                                       verbose= 0)
            masked_data = masker.fit(img_load)
            timeseries =  masker.transform(img_load, confounds=confounds) 

            correlation_matrix = conn_measure.fit_transform([timeseries])[0]

            # add each subject caracteristics to a container
            all_features['condition'].append(cond)
            all_features['subject'].append(sub)
            all_features['connectomes'].append(correlation_matrix)

np.savez_compressed('schaefern100_features', cond = all_features['condition'], sub = all_features['subject'], 
                    conn = all_features['connectomes'])

original = r'/path/to/save/schaefern100_features.npz'
target = r'/new/path/to/save/'

shutil.move(original,target) # change the path of the saved data
