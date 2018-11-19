#!/usr/bin/env python3
# test_rhymed_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules

# Internal modules
from src.rhymed import get_pronunciations, extract_rhyme_phoneme



def test_extract_rhyme_phoneme():

    """
    Test if the function can return a the correct phoneme as expected
    """
    target_phoneme = "AH1 V"
    pronunciation = "L AH1 V"

    phoneme = extract_rhyme_phoneme(pronunciation)

    assert  phoneme == target_phoneme

def test_get_pronunciation():

    """

    Test if get_pronunciation can return the target pronunciation
    """

    given_word = 'love'
    target_pronunciation = 'L AH1 V'

    pronunciation_list = get_pronunciations(given_word)

    assert  target_pronunciation in pronunciation_list


