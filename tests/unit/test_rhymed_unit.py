#!/usr/bin/env python3
# test_rhymed_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules
import pytest
from werkzeug.exceptions import HTTPException
import requests
from flask import make_response, abort

# Testing modules
import src
from src.rhymed import get_rhymed_list , get_pronunciations, extract_rhyme_phoneme



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


def test_get_rhymed_list():

    """
    Test if get_rhymed_list can return a list of words that rhymed with the given word

    """

    given_word = 'love'

    should_included = 'above'

    rhymed_words_list = get_rhymed_list(given_word)

    assert len(rhymed_words_list) > 0
    assert should_included in rhymed_words_list