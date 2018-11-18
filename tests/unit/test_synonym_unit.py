#!/usr/bin/env python3
# test_synonym_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules
import pytest
from werkzeug.exceptions import HTTPException
import requests
from flask import make_response, abort

# Testing modules
import src
from src.synonym import get_one_random , get_synonyms_from_datamuse


def get_sample_validated_words(input_phase,min_interpreting_score=25000):


    datamuse_ml_api_url = 'https://api.datamuse.com/words?ml='


    response = requests.get(datamuse_ml_api_url + input_phase )

    if (response.status_code != 200) or (len(response.text) == 0):
        abort(
            404, "Synonyms can not be found with the given phase: {input_phase}".format(input_phase=input_phase)
        )

    return [word_item['word'] for word_item in response.json() if word_item['score'] > min_interpreting_score]




def test_get_synonyms_from_datamuse():
    """
    Test if the function can return a list of synonyms by given a proper phase
    """
    input_phase = 'very+cold'
    results = get_synonyms_from_datamuse(input_phase)

    assert isinstance(results, list)


def test_get_one_random_synonym():
    """
    Test if the function can return a random synonym as str type by given a proper phase
    """
    input_phase = 'very+cold'
    result = get_one_random(input_phase)

    assert isinstance(result, dict)
    assert len(result) == 1

    # Check if the synonym is in a wider range of list that directly extracted from datamuse ml api
    assert (result['synonym'] in get_sample_validated_words(input_phase))






