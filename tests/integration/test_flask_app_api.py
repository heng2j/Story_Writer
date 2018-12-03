#!/usr/bin/env python3
# test_flask_app_api.py
# ---------------
# Author: Zhongheng Li
# Start Date: 12-1-18
# Last Modified Date: 12-2-18


# System modules
import os
import sys
import unittest

# 3rd party modules
import json

# local modules
import config

from src.rhymed import get_rhymed_list


class MyTestCase(unittest.TestCase):
    def setUp(self):
        config.app.testing = True
        self.app = config.app.test_client()

        # # Load test data
        # self.app = config(db='fixtures/test_basic.json')

    def test_no_argument_synonym(self):
        """
        Test get request on api endpoint /api/synonym/ without argument

        Result: We are expecting a 404 status code from the response

        """

        response = self.app.get('/api/synonym/')

        assert response.status_code == 404
        assert 'The requested URL was not found on the server' in response.json['detail']

    def test_rhymed(self):

        given_word = 'peace'

        rhymed_words_list = get_rhymed_list(given_word)

        # Setting Project Path
        file_dir = os.path.dirname(__file__)
        sys.path.append(file_dir)

        with open(file_dir + '/fixtures/test_rhymed.json', 'r') as f:
            ground_truth_json = json.load(f)

        assert rhymed_words_list == ground_truth_json
        assert len(rhymed_words_list) > 0
