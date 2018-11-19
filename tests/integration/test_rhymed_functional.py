#!/usr/bin/env python3
# test_rhymed_functional.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules

# Internal modules
from src.rhymed import get_rhymed_list


def test_get_rhymed_list():

    """
    Test if get_rhymed_list can return a list of words that rhymed with the given word

    """

    given_word = 'love'

    should_included = 'above'

    rhymed_words_list = get_rhymed_list(given_word)

    assert len(rhymed_words_list) > 0
    assert should_included in  [data['word'] for data in rhymed_words_list]
