#!/usr/bin/env python3
# test_synonym_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules

# Testing modules
from src.synonym import get_one_random, get_synonyms_from_datamuse


def test_get_synonyms_from_datamuse():
    """
    Test if the function can return a list of synonyms by given a proper phase
    """
    input_phase = 'very+cold'
    results = get_synonyms_from_datamuse(input_phase)

    assert isinstance(results, list)
