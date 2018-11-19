#!/usr/bin/env python3
# MetroLyrics_data.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the data tool module and supports all the data management actions
on the Metro Lyrics data set

The original data set can be found from this Kaggle Page:
https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics


"""


# System modules
import os
import re
import csv
import pandas as pd
from config import db

# 3rd party modules
from models import Word

def parse_data_set(data_set_path):


    data_df = pd.read_csv(data_set_path)

    data_df.to_sql(name='songs', con=db.get_engine(), if_exists='append', index=False)


