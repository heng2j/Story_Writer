#!/usr/bin/env python3
# test_synonym_functional.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


# System modules
import unittest

# 3rd party modules
import pytest
from werkzeug.exceptions import HTTPException

# Testing modules
import src
from src.synonym import get_one_random , get_synonyms_from_datamuse




def test_exception_handling_in_synonym(test_client):
    """
    GIVEN a Flask application
    WHEN making a get request to '/api/synonym/{input_phase}'
    THEN check the response to see if it can handle invalid inputs
    """

    input_phase = "12345+asdfg"

    response = test_client.get('/api/synonym/' + input_phase)
    assert response.status_code == 404



