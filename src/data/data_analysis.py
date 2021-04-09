#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""data_cleaning.py: Cleaning of datas for the kaggle competition"""

__author__ = "Fayeulle Mickael"
__copyright__ = "Copyright 2021, Kaggle competition: Zillow"
__credits__ = ["Fayeulle Mickael"]
__version__ = "1.0"
__status__ = "Production"

#Import libraries
import pandas as pd 
import numpy as np
import sys

sys.path.append("../zilow_price")

#Import data
print('Loading data...')

train = pd.read_csv('./Data/raw_data/train_2016_v2.csv')
properties = pd.read_csv('./Data/raw_data/properties_2016.csv') 
sample_df = pd.read_csv('./Data/raw_data/sample_submission.csv')

#Merging properties with the train dataset for exploratory analysis
print('Merging the data...')

df_train = train.merge(properties, how='left', on='parcelid')

#Check the train dataset
print('Our dataset contains {} rows and {} columns.'.format(df_train.shape[0], df_train.shape[1]))

#Checking for missing values
print(df_train.isnull().sum())

#Checking for variables types
