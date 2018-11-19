#!/usr/bin/env python3
# MetroLyrics_data.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-19-18


"""
This is the data tool module and supports all the data management actions
on the Metro Lyrics data set

The original data set can be found from this Kaggle Page:
https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics


"""

# System modules
import os
from os.path import dirname as up

# 3rd party modules
import pandas as pd

# Internal modules
from config import db

from sqlalchemy import create_engine


basedir = up(os.path.abspath(os.path.dirname(__file__)))


def parse_data_set(data_set_path):
    """
    This is used to parse the Metro Lyrics data set with Pandas
    and save the data into our SQLite database

    :param data_set_path: the path to the dataset
    :return:
    """

    data_df = pd.read_csv(data_set_path)

    # Build the Sqlite ULR for SqlAlchemy
    sqlite_url = "sqlite:////" + os.path.join(basedir, "story_writer.db")

    print("sqlite_url: ", sqlite_url)

    engine = create_engine(sqlite_url, echo=False)

    data_df.to_sql(name='songs', con=engine, if_exists='append', index=False)
