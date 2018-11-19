#!/usr/bin/env python3
# test_songs_functional.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-19-18
# Last Modified Date: 11-19-18


# System modules

# Internal modules
from src.songs import get_one_song, create_song, delete_song,create_update_song, update_song
from src.helper_functions import get_timestamp, get_timestamp_year


def test_create_song():
    """
    Test create create new song from song object

    """

    new_song = {
        "artist": "Heng",
        "song": "I can do all things",
        "genre": "Hip-Hop",
        "lyrics": "Like Steph said I can do all things...",
        "year": get_timestamp_year(),
        "timestamp": get_timestamp()
    }

    given_artist = "Heng"
    given_song_title = "I can do all things"

    create_song(new_song)

    song_data = get_one_song(given_artist, given_song_title)

    assert song_data['artist'] == given_artist
    assert song_data['song'] == given_song_title


def test_update_song():
    """
    Test to update existing song

    """

    target_song = {
        "artist": "Heng",
        "song": "I can do all things",
        "genre": "Hip-Hop",
        "lyrics": "Like Steph said I can do all things In...",
        "year": get_timestamp_year(),
        "timestamp": get_timestamp()
    }

    update_song(target_song)

    updated_song_lyrics = "Like Steph said I can do all things In..."

    given_artist = "Heng"
    given_song_title = "I can do all things"

    song_data = get_one_song(given_artist, given_song_title)

    print("updated_song_data['lyrics']: ", song_data['lyrics'])

    assert song_data['lyrics'] == updated_song_lyrics


def test_delete_song():
    """
    Test to delete song

    """

    target_song = {
        "artist": "Heng",
        "song": "I can do all things",
        "genre": "Hip-Hop",
        "lyrics": "Like Steph said I can do all things...",
        "year": get_timestamp_year(),
        "timestamp": get_timestamp()
    }

    make_response, code = delete_song(target_song)

    assert make_response == "The song title I can do all things is deleted for artist: Heng."


def test_create_update_Song():
    """
    Test to create new song, and update instead if the song is already exist. (Upsert)
    """

    target_song = {
        "artist": "Heng",
        "song": "I can do all things (Remix)",
        "genre": "Hip-Hop",
        "lyrics": "Like Steph said I can do all things...",
        "year": get_timestamp_year(),
        "timestamp": get_timestamp()
    }

    given_artist = "Heng"
    given_song_title = "I can do all things (Remix)"

    create_update_song(target_song)

    song_data = get_one_song(given_artist, given_song_title)

    assert song_data['artist'] == given_artist
    assert song_data['song'] == given_song_title
