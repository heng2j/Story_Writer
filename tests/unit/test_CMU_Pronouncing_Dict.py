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
import pytest
from werkzeug.exceptions import HTTPException
import requests
from flask import make_response, abort

# Testing modules
from src.data_tools.CMU_Pronouncing_Dict import extract_rhyme_phoneme , parse_data_set



projectPath = os.getcwd()


def test_extract_rhyme_phoneme():

    """
    Test if the function can return a the correct phoneme as expected
    """
    target_phoneme = "AH1 V"
    pronunciation = "L AH1 V"

    phoneme = extract_rhyme_phoneme(pronunciation)

    assert  phoneme == target_phoneme


def test_pronunciations_list():

    """
    Test if the function can return a pronunciations list
    """
    print("projectPath: ", up(up(projectPath)))

    data_set_path = "/data/cmudict-0.7b"

    pronunciations_list = parse_data_set(up(up(projectPath)) + data_set_path)

    assert  isinstance(pronunciations_list,list)
