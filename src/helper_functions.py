#!/usr/bin/env python3
# helper_functions.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-19-18
# Last Modified Date: 11-19-18


"""
This is the helper functions module that contain all the helper functions across this project


"""

# System modules
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def get_timestamp_year():
    return datetime.now().year
