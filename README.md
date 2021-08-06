
# About me
<img src="https://avatars.githubusercontent.com/u/86985765?v=4?s=100" width="100px;" alt=""/>
<href="https://github.com/catherinelandry"> 

  [Catherine Landry (she/her)](https://github.com/catherinelandry)

  Hello! I am currently doing my master's degree in psychology at the University of Montreal. My wide range of interests is reflected through my eclectic research background. I have worked with children at Sainte-Justine Hospital, trained spinal cord injured rats, and I am now doing research on individuals living with deafness. As of today, I'm particularly hyped about neuroimaging and coding, hence my learning journey with PSY6983. 


# Project Definition

## Background

Functional connectivity can be studied at different resolutions, scaling from locally functional areas to large and spatially distributed networks. At rest, brain regions with correlated temporal patterns with each other form resting state networks (RSN).  

Sensory deprivation leads to functional changes in the brain beyond the affected sensory modality. Various studies have found altered RSN in deaf individuals compared to controls (e.g., [Bonna et al., 2020](https://doi.org/10.1007/s11682-020-00346-y); [Ducas et al., 2021](https://doi.org/10.21203/rs.3.rs-246296/v1)). 

**Main objective:**

Supervised machine learning can yield characterization of rs-fMRI for individual-level predictions [Khosla et al., 2019](https://doi.org/10.1016/j.mri.2019.05.031)). Therefore, this project aims to determine the most contributing features in machine learning prediction at single-participant level. The achieving goal would be to interpret the coefficients in accordance to the RSN. 
 
 ![Main objective](readme.png)
 
 <p> <font size="1">Source: Illustration created with Selman Design taken in Autodraw under the license CC BY 4.0 </font></p> 
 

**Personal objectives set for the class:**

* Familiarize myself with open science software and best practices 

* Understand the neuroimaging workflow from preprocessing to data visualization

* Learn how to code confidently with python 

* Have a better understanding of machine learning and its application in neuroimaging 

## Tools

All the tools used for the project: 

* Bash Terminal 

* Visual Studio Code 

* Jupyter Notebook  
  
* Git and Github for version control 

* [BIDS Validator](https://bids-standard.github.io/bids-validator/) web browser based version

* [`matplotlib`](https://matplotlib.org/), [`seaborn`](https://seaborn.pydata.org/), [`plotly`](https://plotly.com/), and [`ipywidgets`](https://ipywidgets.readthedocs.io/en/latest/) for Data Visualization

* [`scikit-learn`](https://scikit-learn.org/stable/) and [`nilearn`](https://nilearn.github.io/) for Machine Learning and Statistic Analyses

## Data

### Overal view 
The dataset comprises 5-minutes fMRI resting state images covering the whole brain of 35 adult participants, 17 of which have severe-to-profound prelingual deafness and 18 of which are hearing individuals that serve as controls. All participants were instructed to lie still with closed eyes and to avoid holding on to thoughts for the duration of the scanning. 

Here is a summary table of some participants' characteristics.

|                 |Age (Mean±STD)|  Sex (F/M)   |Education (yrs)| Handedness |  
|-----------------|:------------:|:------------:|:-------------:|:----------:|  
|control (n=18)   |  29.89±5.27  |     13/5     |  16.9         | 15 right   |   
|deaf    (n=17)   |  30.35±4.57  |     12/5     |  15.3         | 12 right   |

For further questions on the dataset and the acquisition parameters, I encourage you to reach out to me at cath.landry2@gmail.com


## Deliverables

At the end of this project, I will have:

* README file for the project repository 
* Markdown document for my trial and error journal
* requirements.txt that lists all the packages used in the project
* Jupiter notebooks for the presentation slides and data visualization
* Python scripts for data prep and machine learning

Detailed instructions on how to use each file can be found here (soon available). 

## References

Bonna, K., Finc, K., Zimmermann, M., Bola, L., Mostowski, P., Szul, M., Rutkowski, P., Duch, W., Marchewka, A., Jednorog, K., & Szwed, M. (2020). Early deafness leads to re-shaping of functional connectivity beyond the auditory cortex. Brain Imaging and Behavior, 1-14. https://doi.org/10.1007/s11682-020-00346-y 

Ducas, K. D., Senra Filho, A. C. D. S., Silva, P. H. R., Secchinato, K. F., Leoni, R. F., & Santos, A. C. (2021). Functional and structural brain connectivity in congenital deafness. Brain Structure and Function, 226(4), 1323-1333. https://doi.org/10.21203/rs.3.rs-246296/v1 

Khosla, M., Jamison, K., Ngo, G. H., Kuceyeski, A., & Sabuncu, M. R. (2019). Machine learning in resting-state fMRI analysis. Magnetic resonance imaging, 64, 101-121. https://doi.org/10.1016/j.mri.2019.05.031
