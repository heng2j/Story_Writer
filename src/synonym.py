#!/usr/bin/env python3
# synonym.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-17-18


"""
This is the synonym module and supports all the ReST actions for the
synonym collection

"""


# System modules
import requests

# 3rd party modules
from flask import make_response, abort



def get_one_random(word_list):



    """
    This function

    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data


    requests = ""

    resp = requests.get('https://todolist.example.com/tasks/')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    for todo_item in resp.json():



    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]