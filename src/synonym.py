#!/usr/bin/env python3
# synonym.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-18-18


"""
This is the synonym module and supports all the ReST actions for the
synonym collection

"""


# System modules
import random

# 3rd party modules
import requests
from flask import make_response, abort


def get_synonyms_from_datamuse(word_list, max_num=20 , min_interpreting_score=25000 ):

    """
    :param word_list: A list of string to query the datamuse Means like(ml) endpoint for synonyms
    :param max_num: Max return result. Set to 20 by default
    :param min_interpreting_score: Minimum interpreting score to select the most relevant synonyms. Set to 25000 by default
    :return: A list of synonyms where the interpreting score is higher than the min_interpreting_score
    """

    datamuse_ml_api_url = 'https://api.datamuse.com/words?ml='

    values = "+".join([word for word in word_list])

    max_num_str = '&max=' + str(max_num)

    response = requests.get(datamuse_ml_api_url + values + max_num_str)

    if (response.status_code != 200) or (len(response.text) == 0):

        abort(
            404, "Synonyms can not be found with the given phase: {word_list}".format(word_list=word_list)
        )


    return [ word_item['word'] for word_item in response.json() if word_item['score'] > min_interpreting_score]


def get_one_random(word_list):

    """
    :param word_list: A list of string to query the datamuse Means like(ml) endpoint for synonyms
    :return: A random choice from the synonyms that returned from get_synonyms_from_datamuse
    """

    synonyms = get_synonyms_from_datamuse(word_list, max_num=20)

    return random.choice(synonyms)
