#!/usr/bin/env python3
# CMU_Pronouncing_Dict.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the data tool module and supports all the data management actions
on the CMU Pronouncing Dictionary data set


"""

# System modules
import os
from os.path import dirname as up

# Internal modules
from rhymed import extract_rhyme_phoneme

# 3rd party modules
import pandas as pd
from sqlalchemy import create_engine

basedir = up(os.path.abspath(os.path.dirname(__file__)))


def parse_data_set(data_set_path):
    """
    Extract words and associated pronunciations line by line from the data set
        - Extract rhyme phonemes from pronunciations as mentioned in this post: https://stackoverflow.com/questions/15822832/rhyme-dictionary-from-cmu-pronunciation-database
            - Rhyme phoneme has primary stress (numbered as 1). So we are going to extract
              the sub-string that start from a string that contains the number "1" in that
              pronunciation to the end of the pronunciation string
        - If there are more than one pronunciation for a word, append the tuple of (word,pronunciation,phoneme)
          into the pronunciations_list. Which will be a better structure for later database insertion and selection
    Store the word and list of rhyme phonemes in to the dictionary pronunciation_dict


    :param data_set_path: Path to the CMU Pronouncing Dictionary data set
    :return: pronunciations_list. A list of all the words mentioned in the
             CMU Pronouncing Dictionary data set along with their pronunciation and rhyme phoneme
    """

    pronunciations_list = []

    # For parsing the cmudict-0.7b file, we has to use encoding "ISO-8859-1" to avoid UnicodeDecodeError
    with open(data_set_path, encoding="ISO-8859-1") as dataFile:
        for row in dataFile:
            row = row.strip()
            if not row.startswith(';'):
                word, pronunciation = row.split("  ")
                word = word.rstrip("(0123)").lower()

                phoneme = extract_rhyme_phoneme(pronunciation)

                pronunciations_list.append((word, pronunciation, phoneme))

    return pronunciations_list


def save_data_to_database_with_pandas(data_in_list):
    columns = ['word', 'pronunciation', 'phoneme']
    data_df = pd.DataFrame.from_records(data_in_list, columns=columns)

    # Build the Sqlite ULR for SqlAlchemy
    sqlite_url = "sqlite:////" + os.path.join(basedir, "story_writer.db")

    engine = create_engine(sqlite_url, echo=False)

    data_df.to_sql(name='words', con=engine, if_exists='append', index=False)
