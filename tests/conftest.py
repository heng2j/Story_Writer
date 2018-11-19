#!/usr/bin/env python3
# conftest.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-17-18
# Last Modified Date: 11-18-18


# System modules

# 3rd party modules
import pytest

# Testing modules
import src.server as server


@pytest.fixture(scope='module')
def test_client():
    """
    This code are originally covered from this blog post: https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

    GitLab Repo: https://gitlab.com/patkennedy79/flask_user_management_example/blob/master/tests/conftest.py

    :return:
    """

    flask_app = server.create_app('flask_test.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
