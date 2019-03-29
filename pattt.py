# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:34:49 2019

@author: NPL
"""
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# define a corpus

corpus = ["I love BO","lily not","lily why happening"]
corpus
tempvar = CountVectorizer()
tempvar3 = tempvar.fit_transform(corpus)
print(tempvar3)
vard = tempvar.get_feature_names()

print(tempvar.get_feature_names())
tempvar3.todense()
hh = pd.DataFrame(tempvar3.todense(),index = ['line1','b','c'],columns = tempvar.get_feature_names())######mapped features
hh
#####################################
import importlib
########################
dir(importlib)
importlib.__all__
##############################





##############################
import platform
print(platform.python_version())
#########################
import  importlib.util as df
import  matplotlib


import importlib.utils as mn
importlib.util.find_spec(name, package=None)

dir(matplotlib)
