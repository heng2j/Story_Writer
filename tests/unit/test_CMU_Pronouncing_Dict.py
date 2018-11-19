#!/usr/bin/env python3
# test_CMU_Pronouncing_Dict_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


# System modules
import os
from os.path import dirname as up

# 3rd party modules

# Testing modules
from src.data_tools.CMU_Pronouncing_Dict import parse_data_set

projectPath = os.getcwd()


def test_pronunciations_list():
    """
    Test if the function can return a pronunciations list
    """

    data_set_path = up(up(projectPath)) + "/data/cmudict-0.7b"

    print("data_set_path: ", data_set_path)

    pronunciations_list = parse_data_set(data_set_path)

    assert isinstance(pronunciations_list, list)

    assert len(pronunciations_list) == 134371
