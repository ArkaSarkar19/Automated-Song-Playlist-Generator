# Personalised-Song-Playlist-Generator
by **Arka Sarkar, Pankil Kalra and Daksh Thapar** from **Indraprastha Institute of Information Technology, Delhi**. 

### Introduction 
With the growing popularity of music streaming services like Spotify, Apple Music and Wynk, the number of songs have skyrocketed globally. Creating personalized playlists for users has become tedious and challenging as it involves individual listening to various songs and categorizing them based on their audio features. The objective is to sort songs with similar musical characteristics into playlists  automatically. Modern machine learning techniques and visualization tools should help us find accurate models that categorize millions of songs into user playlists based on song choices. Related works on this problem did not consider Lyrical Analysis while making playlists. We are using Topic Modelling techniques on lyrics, and will be using the extracted topics as a feature for generating playlists.

### Description and Implementation Details
In this repository, we have implemented vairous machine learning aglorithms on Topic Extracted from the lyrical corpus. </br>

  * DataScrape - Dataset, Data Collecction code, pre-processing and topic modeling </br>
  * PreProcessing - Code for Visualisation 
  * models - binary classification , multi classification , clustering, K-nearest Neighbours source code with the respective models saved with the results also saved. 


### How to Run ? 
The models pickles are saved in "rb" format in their respeective directories (\models directory). 
  * To load the models
 
        f = open("model_name", "rb")
        load_model = pickle.load(f)
        f.close()
    
    
  * To test the models 
    * Clustering Models - They are simple pickled files of the models which can be executed and evaluated by the  following code .
          
          model.predict(X_test)
          
    * Multi classification Models - hey are simple pickled files of the models which can be executed and evaluated by the following code.
    
          model.predict(X_test)
          
    * Binary Classification Models - It is a list of all the one vs all models which can be executed and evaluated using the following code.

           pred = []
           for i in range(len(load_model)):
               pred.append(load_model[i].predict(X_test))

           pred.argmax(axis = 1)
           
   * Generate Graphs for the Analysis
     * Each graph can be plotted from the *ipynb* files in the directories, the code is documented for one to understand and plot the respective graphs. 
     
### Installed dependencies 
    python 3.7
    jupyter notebook.
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LogisticRegression, SGDClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import precision_score
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    from sklearn.metrics import balanced_accuracy_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import recall_score
    from tqdm import tqdm
    from imblearn.ensemble import BalancedBaggingClassifier
    from imblearn.under_sampling import RandomUnderSampler
    from sklearn.svm import SVC
    from xgboost import XGBClassifier
    import pickle
    import tensorflow as tf
    import math
    import keras
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    import xgboost as xgb
    from xgboost.sklearn import XGBClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import OneHotEncoder
    from sklearn import preprocessing
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from matplotlib import pyplot as plt
    from sklearn.metrics import silhouette_samples
    import matplotlib.cm as cm
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE
    import seaborn as sns
    from sklearn.decomposition import TruncatedSVD
    from sklearn.cluster import DBSCAN
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.cluster import SpectralClustering
    import pyLDAvis
    import pyLDAvis.gensim
    
### Contact 
For any furhter queries feel free to reach out the following contributors. 

Pankil Kalra (pankil18061@iiitd.ac.in) </br>
Daksh Thapar (daksh18137@iiitd.ac.in) </br>
Arka Sarkar (arka18222@iiitd.ac.in) </br>

Machine Learning- CSE343, ECE343
