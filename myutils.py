import numpy as np
np.set_printoptions(precision = 4, 
                    threshold = 1000, 
                    linewidth = np.inf, 
                    formatter = {"float_kind":"{:7.4f}".format})


import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['figure.figsize']  = (10, 8)

try:
    import seaborn as sns
   
    sns.set_theme(
        palette = "bright", 
        font_scale = 1.1,
        )
except:
    pass

import plotly.express as px

import pandas as pd
def read_sheets(url, decimal = ",", **kwargs):
    url = url.replace('/edit#gid=', '/export?format=tsv&gid=')
    df  = pd.read_csv(url,
                      sep = "\t",
                      decimal = decimal,
                      **kwargs)
    return df
pd.set_option('display.max_columns', 50)


from datetime import datetime
from glob     import glob
from time     import time, sleep
from PIL      import Image

import os
import re

def download_drive(url, unzip = True):
    id = re.findall("d/([\S]*)/", url)[0]

    export_url = '"https://drive.google.com/uc?export=download&id={}&confirm=no_antivirus"'.format(id)
    
    if unzip:
        os.system("gdown {} -O temp.zip".format(export_url))
        os.system("unzip temp.zip")
        os.system("rm temp.zip")
    else:
        os.system("gdown {} ".format(export_url))
        
    return