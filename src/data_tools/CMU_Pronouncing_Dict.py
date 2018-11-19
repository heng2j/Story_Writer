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
import re
from config import db

# 3rd party modules
from models import Word



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
    with open(data_set_path, encoding = "ISO-8859-1") as dataFile:
        for row in dataFile:
            row = row.strip()
            if not row.startswith(';'):
                word, pronunciation = row.split("  ")
                word = word.rstrip("(0123)").lower()

                phoneme = extract_rhyme_phoneme(pronunciation)

                pronunciations_list.append((word, pronunciation, phoneme))


    return pronunciations_list


def save_data_to_database(pronunciations_list):
    """

    :param pronunciations_list:
    :return:
    """

    # Delete database file if it exists currently
    if os.path.exists("word.db"):
        os.remove("word.db")

    # Create the database
    db.create_all()

    # iterate over the PEOPLE structure and populate the database
    for word in pronunciations_list:
        p = Word(word=word[0], pronunciation=word[1], phoneme=word[2])
        db.session.add(p)

    db.session.commit()



