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
from src.rhymed import get_rhymed_list
