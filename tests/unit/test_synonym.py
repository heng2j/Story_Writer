#!/usr/bin/env python3
# test_synonym.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules
import pytest
from werkzeug.exceptions import HTTPException

# Testing modules
import src
from src.synonym import get_one_random , get_synonyms_from_datamuse


def test_get_synonyms_from_datamuse():
    """
    Test if the function can return a list of synonyms by given a proper phase
    """
    word_list = ['very', 'cold']
    results = get_synonyms_from_datamuse(word_list)

    assert isinstance(results, list)


def test_get_one_random_synonym():
    """
    Test if the function can return a random synonym as str type by given a proper phase
    """
    word_list = ['very', 'cold']
    result = get_one_random(word_list)

    assert isinstance(result, str)

