# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:25:57 2022
@author: ialav
"""


import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#pd.set_option('display.max_rows', None)

#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', 2000)
#from statsmodels.tsa.seasonal import seasonal_decompose


def ELOP(url):
    
    df = pd.read_excel(url, skiprows= range(0,4))
    df = df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Unidad'})
    df=df.iloc[ :,0:2]
    df=df.dropna()
    X=df.iloc[:,0]
    Y=df.iloc[:,1]
    sns.set(font_scale=1.5, rc={'axes.facecolor':'pink','figure.facecolor':'gray'})
    sns.lineplot(x=X, y= Y, data=df, )
    sns.set(style='dark',)
    plt.savefig('ELOP')
    

ELOP("https://www.ine.gub.uy/c/document_library/get_file?uuid=0c0fbfd5-d4ab-4414-96cd-dbff821e4b00&groupId=10181")