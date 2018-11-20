#!/usr/bin/env python3
# build_database.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the build database module to create the SQLite database

"""

# System modules
import os
from os.path import dirname as up
from config import db

# Internal modules
from models import Word
from data_tools import CMU_Pronouncing_Dict as CMU_data_tools
from data_tools import MetroLyrics_data as MetroLyrics_data_tools

projectPath = os.getcwd()


def build_database_for_CMU_Pronouncing_Dict(cmu_file_path):
    data_set_path = up(projectPath) + cmu_file_path

    pronunciations_list = CMU_data_tools.parse_data_set(data_set_path)

    CMU_data_tools.save_data_to_database_with_pandas(pronunciations_list)


    # # iterate over the pronunciations_list and populate the database
    # for word in pronunciations_list:
    #     p = Word(word=word[0], pronunciation=word[1], phoneme=word[2])
    #     db.session.add(p)
    #
    # db.session.commit()


def build_database_for_Lyrics(lyrics_file_path):
    data_set_path = up(projectPath) + lyrics_file_path

    MetroLyrics_data_tools.parse_data_set(data_set_path)


# Delete database file if it exists currently
if os.path.exists("story_writer.db"):
    os.remove("story_writer.db")

# Create the database
db.create_all()

cmu_file_path = "/data/cmudict-0.7b"
build_database_for_CMU_Pronouncing_Dict(cmu_file_path)

lyrics_file_path = "/data/lyrics_hiphop.csv"
build_database_for_Lyrics(lyrics_file_path)
