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
    __tablename__ = "words"
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


class Song(db.Model):
    __tablename__ = "songs"
    song_id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(32))
    year = db.Column(db.Integer)
    artist = db.Column(db.String(128))
    genre = db.Column(db.String(32))
    lyrics = db.Column(db.Text()) # text
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class SongSchema(ma.ModelSchema):
    class Meta:
        model = Song
        sqla_session = db.session