#!/usr/bin/env python3
# CMU_Pronouncing_Dict.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-18-18


"""
This is the data tool module and supports all the data management actions
on the CMU Pronouncing Dictionary data set


"""


# System modules


# 3rd party modules


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


def parse_data_set(data_set_path):
    """
    Extract words and associated pronunciations line by line from the data set
        - Extract rhyme phonemes from pronunciations as mentioned in this post: https://stackoverflow.com/questions/15822832/rhyme-dictionary-from-cmu-pronunciation-database
            - Rhyme phoneme has primary stress (numbered as 1). So we are going to extract
              the sub-string that start from a string that contains the number "1" in that
              pronunciation to the end of the pronunciation string
        - If there are more than one pronunciation for a word, append the tuple of (word,pronunciation,phoneme)
          into the pronunciations_list. Which will be a better structure for later database insertion and selection
    Store the word and list of rhyme phonemes in to the dictionary pronunciation_dict


    :param data_set_path: Path to the CMU Pronouncing Dictionary data set
    :return: pronunciations_list. A list of all the words mentioned in the
             CMU Pronouncing Dictionary data set along with their pronunciation and rhyme phoneme
    """

    pronunciations_list = []

    with open(data_set_path) as dataFile:

        line = dataFile.readline()
        line = line.strip()
        if not line.startswith(';'):

            word , pronunciation = line.split("  ")
            word = word.rstrip("(0123)").lower()

            phoneme = extract_rhyme_phoneme(pronunciation)

            pronunciations_list.append((word,pronunciation,phoneme))

    return pronunciations_list


    # def save_data_to_databae(pronunciations_list):
    #
    #
    #
    #     return None
