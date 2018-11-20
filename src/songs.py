#!/usr/bin/env python3
# songs.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-18-18
# Last Modified Date: 11-19-18


"""
This is the songs module and supports all the ReST actions for the
songs collection

"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
from sqlalchemy import and_, update
from  sqlalchemy.sql.expression import func

# Internal modules
from models import Song, SongSchema
from config import db

import helper_functions


def get_one_song(artist, song_title):
    """

    :param artist:
    :param song_title:
    :return:
    """

    # Get the song requested
    song = Song.query.filter(and_(Song.artist == artist, Song.song == song_title)).one_or_none()

    # Did we find a song?
    if song is not None:

        # Serialize the data for the response
        song_schema = SongSchema()
        data = song_schema.dump(song).data
        return data

    # Otherwise, nope, didn't find that song
    else:
        abort(
            404,
            "Song title {song_title} is not found for artist: {artist} ".format(artist=artist, song_title=song_title),
        )
        return None


def get_one_song_by_id(song_id):
    """

    :param song_id:
    :return:
    """

    # Get the song requested
    song = Song.query.filter(Song.song_id == song_id).one_or_none()

    # Did we find a song?
    if song is not None:

        # Serialize the data for the response
        song_schema = SongSchema()
        data = song_schema.dump(song).data
        return data

    # Otherwise, nope, didn't find that song
    else:
        abort(
            404,
            "Song is not found for song id: {song_id} ".format(song_id=song_id),
        )
        return None


def get_partial_match_substring(lyrics_str, given_word):

    """

    :param lyrics_str:
    :param given_word:
    :return:
    """

    word_list = lyrics_str.split()

    for i in range(len(word_list) - 1, 0, -1):
        if given_word in word_list[i]:
            return " ".join(word_list[i - 10: i + 10])


def get_top_sample_lyrics(given_word, limits=10):
    """

    :param given_word:
    :param limits:
    :return:
    """

    # Get the songs requested
    songs = Song.query.filter(and_(Song.lyrics.like(f'%{given_word}%'),Song.lyrics != None)).order_by(func.random()).limit(limits).all()

    # Did we find a the songs?
    if songs is not None:

        # Serialize the data for the response
        song_schema = SongSchema(many=True)
        song_data = song_schema.dump(songs).data

        for data in song_data:
            data['lyrics'] = get_partial_match_substring(data['lyrics'], given_word)

        return song_data

    # Otherwise, nope, didn't find any song
    else:
        abort(
            404,
            "Songs not found for given word: {given_word}".format(given_word=given_word),
        )


def create_song(song):
    """
    This function creates a new song in the song structure
    based on the passed in song data
    :param song:  song to create in song structure
    :return:        201 on success create new song
    """
    song_title = song['song']
    artist = song['artist']

    existing_song = (
        Song.query.filter(Song.song == song_title)
            .filter(Song.artist == artist)
            .one_or_none()
    )

    # Can we insert this song?
    if existing_song is None:

        # Create a song instance using the schema and the passed in song
        schema = SongSchema()
        new_song = schema.load(song, session=db.session).data

        # Add the song to the database
        db.session.add(new_song)
        db.session.commit()

        # Serialize and return the newly created song in the response
        data = schema.dump(new_song).data

        return data, 201

    # Otherwise, update existing song
    else:
        abort(
            409,

            "Song title {song_title} is already exists for artist: {artist} ".format(artist=artist,
                                                                                     song_title=song_title),
        )


def update_song(song):
    """
    This function update a existing song in the song structure
    based on the passed in song data
    :param song:  song to update in song structure
    :return:      200 on success update song
    """
    song_title = song['song']
    artist = song['artist']

    existing_song = (
        Song.query.filter(Song.song == song_title)
            .filter(Song.artist == artist)
            .one_or_none()
    )

    # Did we find a song?
    if existing_song is not None:

        existing_song.song = song['song']
        existing_song.artist = song['artist']
        existing_song.lyrics = song['lyrics']
        existing_song.year = helper_functions.get_timestamp_year()
        existing_song.timestamp = datetime.now()

        # turn the passed in song into a db object
        schema = SongSchema()

        # Commit new updates
        db.session.commit()

        # return updated song in the response
        data = schema.dump(existing_song).data

        return data, 200

    # Otherwise, nope, didn't find that song
    else:
        abort(
            404,
            "Song title {song_title} is not found for artist: {artist} ".format(artist=artist, song_title=song_title),
        )


def create_update_song(song):
    """
        This function will create a new song if it is not already exist in the song structure.
        If the song is exist, it will update the song instead.
        based on the passed in song data
        :param song:  song to create in song structure
        :return:        201 on success create new song , 200 on success update song
        """
    song_title = song['song']
    artist = song['artist']

    existing_song = Song.query.filter(Song.song == song_title).filter(Song.artist == artist).one_or_none()

    # Is this song already exist?
    if existing_song is None:

        # Create a song instance using the schema and the passed in song
        schema = SongSchema()
        new_song = schema.load(song, session=db.session).data

        new_song.year = helper_functions.get_timestamp_year()
        new_song.timestamp = datetime.now()

        # Add the song to the database
        db.session.add(new_song)
        db.session.commit()

        # Serialize and return the newly created song in the response
        data = schema.dump(new_song).data

        return data, 201

    # If the song is already exist, update the song instead
    else:

        print("existing_song: ", existing_song)

        existing_song.song = song['song']
        existing_song.artist = song['artist']
        existing_song.lyrics = song['lyrics']
        existing_song.year = helper_functions.get_timestamp_year()
        existing_song.timestamp = datetime.now()

        # turn the passed in song into a db object
        schema = SongSchema()

        # Commit new updates
        db.session.commit()

        # return updated song in the response
        data = schema.dump(existing_song).data

        return data, 200


def delete_song(target_song):
    """
    This function deletes a song from the song structure
    :param song:   the song object to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the song requested
    songs = Song.query.filter(and_(Song.artist == target_song['artist'], Song.song == target_song['song'])).all()

    print("song: ", songs)

    # Did we find a song?
    if songs is not None:

        for song in songs:
            print("song song_id:", song.song_id)

            db.session.delete(song)
            db.session.commit()

        return "The song title {song_title} is deleted for artist: {artist}.".format(artist=target_song['artist'],
                                                                                     song_title=target_song[
                                                                                         'song']), 200

        # return make_response(
        #     "The song title {song_title} is deleted for artist: {artist}.".format(artist=target_song['artist'],song_title=target_song['song']), 200
        # )


    # Otherwise, nope, didn't find this song
    else:
        abort(
            404,
            "Song title {song_title} is not found for artist: {artist} ".format(artist=target_song['artist'],
                                                                                song_title=target_song['song']),
        )


def delete_song_by_id(song_id):
    """
    This function deletes a song from the song structure
    :param song:   the song id of the song object to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the song requested
    songs = Song.query.filter(Song.song_id == song_id).all()

    print("song: ", songs)

    # Did we find a song?
    if songs is not None:

        for song in songs:
            print("song song_id:", song.song_id)

            db.session.delete(song)
            db.session.commit()

        return "The song with song id {song_id} is deleted.".format(song_id=song_id), 200

        # return make_response(
        #     "The song title {song_title} is deleted for artist: {artist}.".format(artist=target_song['artist'],song_title=target_song['song']), 200
        # )


    # Otherwise, nope, didn't find this song
    else:
        abort(
            404,
            "Song with song id {song_id} is not found.".format(song_id=song_id),
        )
