#!/usr/bin/env python3
# server.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 12-12-18


"""
Main module of the server file
"""

# System modules
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


# 3rd party moudles
from flask import render_template


# local modules
import config as config


def create_app():
    # Get the application instance
    connex_app = config.connex_app

    # Read the swagger.yml file to configure the endpoints
    connex_app.add_api("swagger.yml")

    return connex_app

connex_app = create_app()


# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":



    connex_app.run(debug=True)


