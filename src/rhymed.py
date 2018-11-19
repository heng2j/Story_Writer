#!/usr/bin/env python3
# rhymed.py
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
import requests
from flask import make_response, abort

# Internal modules
from models import Word , WordSchema
from sqlalchemy import and_


def extract_rhyme_phoneme(pronunciation):
    """

    :param pronunciation: a string representation of the pronunciation
    :return: a string of rhyme phoneme extract from the pronunciation string
    """

    phoneme_list = pronunciation.split()

    for i in range(len(phoneme_list) - 1, 0 , -1):
        if phoneme_list[i][-1] in '12':
            return " ".join(phoneme_list[i:])

    return None


def get_pronunciations(given_word):

    """

    :param given_word: Take a string as a given_word
    :return: A list of all the possible pronunciations from the given_word
    """


    # Get the word requested
    words = Word.query.filter(Word.word == given_word).all()

    # Did we find a the word?
    if words is not None:

        # Serialize the data for the response
        word_schema = WordSchema(many=True)
        word_data = word_schema.dump(words).data

        return [ data['pronunciation']  for data in word_data]

    # Otherwise, nope, didn't find that word
    else:
        abort(
            404,
            "Pronunciation not found for given word: {given_word}".format(given_word=given_word),
        )





def get_rhymed_list(given_word):
    """

    :param given_word:
    :return:
    """

    pronunciation_list = get_pronunciations(given_word)

    rhyme_phoneme_list = [ rhyme_phoneme for rhyme_phoneme in map(extract_rhyme_phoneme,pronunciation_list)]

    print("rhyme_phoneme_list: ", rhyme_phoneme_list)

    # Get the word requested
    words = Word.query.filter(and_(Word.phoneme.in_(rhyme_phoneme_list) ,Word.word!=given_word )).all()

    # Did we find a the word?
    if len(words) != 0:

        # Serialize the data for the response
        word_schema = WordSchema(many=True)
        word_data = word_schema.dump(words).data

        print("word_data: ", word_data)

        return [data['word'] for data in word_data]

    # Otherwise, nope, didn't find that word
    else:
        abort(
            404,
            "Pronunciation not found for given word: {given_word}".format(given_word=given_word),
        )


    return []
