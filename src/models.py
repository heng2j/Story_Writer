#!/usr/bin/env python3
# models.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the models module that store the schema for the objects that we are using in this project


"""


# System modules
from datetime import datetime
from config import db, ma

# 3rd party modules



class Word(db.Model):
    __tablename__ = "word"
    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(32))
    pronunciation = db.Column(db.String(32))
    phoneme = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class WordSchema(ma.ModelSchema):
    class Meta:
        model = Word
        sqla_session = db.session