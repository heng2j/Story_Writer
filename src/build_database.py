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



projectPath = os.getcwd()

data_set_path = up(projectPath) + "/data/cmudict-0.7b"


pronunciations_list = CMU_data_tools.parse_data_set(data_set_path)

print(len(pronunciations_list))

# CMU_data_tools.save_data_to_database(pronunciations_list)







# # Delete database file if it exists currently
# if os.path.exists("word.db"):
#     os.remove("word.db")
#
#
#
# # Create the database
# db.create_all()
#
# pronunciations_list = [('ABOVE','AH0 B AH1 V','AH1 V'),('LOVE','L AH1 V','AH1 V') ]
#
# # iterate over the PEOPLE structure and populate the database
# for word in pronunciations_list:
#     p = Word(word=word[0], pronunciation=word[1], phoneme=word[2])
#     db.session.add(p)
#
# db.session.commit()