#!/usr/bin/env python3
# songs.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the rhymed module and supports all the ReST actions for the
rhymed collection

"""

# System modules

# 3rd party modules
from flask import make_response, abort

# Internal modules
from models import Song,SongSchema


def get_one_sample_lyrics(given_word):

    lyrics = ""
    return lyrics

def get_partial_match_substring(lyrics_str,given_word):

    word_list = lyrics_str.split()

    for i in range(len(word_list) - 1, 0 , -1):
        if given_word in word_list[i]:
            return " ".join(word_list[i - 10 : i  + 10])




def get_top_sample_lyrics(given_word, limits = 10):


    # Get the songs requested
    songs = Song.query.filter(Song.lyrics.like(f'%{given_word}%') ).limit(limits).all()

    # Did we find a the songs?
    if songs is not None:

        # Serialize the data for the response
        song_schema = SongSchema(many=True)
        song_data = song_schema.dump(songs).data

        for data in song_data:

            data['lyrics'] = get_partial_match_substring(data['lyrics'],given_word)


        return song_data

    # Otherwise, nope, didn't find any song
    else:
        abort(
            404,
            "Songs not found for given word: {given_word}".format(given_word=given_word),
        )
