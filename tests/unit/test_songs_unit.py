#!/usr/bin/env python3
# test_songs_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-19-18
# Last Modified Date: 11-19-18


# System modules

# Internal modules
from src.songs import get_partial_match_substring ,get_top_sample_lyrics , get_one_song, create_song, delete_song , create_update_song ,update_song , get_one_song_by_id
from src.helper_functions import get_timestamp , get_timestamp_year


def test_partial_match_substring():

    """
    Test getting partial match Substring


    """

    given_word = "god"

    sample_lyrics = """

    (chorus)
    Timbo- When you hit me on my phone betta know what cha want, when you call me, you already know, on the low, im sayin Hey! i got that(dro). I got that(drank). I got that(?). I got. I gotta pocket fulla stones and im playin the corner, you want it, you already know, you sicko. Im sayin Hey!.about that. Hey!.about that. Hey!.about that. Hey! about. whoo!
    (verse 1)
    Lil Eazy E- Lemme tell you bout a nigga name E (name E). Im hittin corners in compton and movin work gettin profit, they tryna stop it but im so low key (low key). They say with dollars come power, im stackin mine by the hour, man fuck that coward! Ima, get while the gettin's good, Got boyz in da hood, and bundles of Kush, Muthafucka George Bush! See he aint helpin us, the streets they respectin us, Government aint tryna help, so we just invest in us. Do whatever for a buck, in the hustle i trust, moved from the back of the bus to a Maybach in a tux. Livin that good life(life). Still Lovin that hood life(life). This for my homies who locked down and doin life.
    They not on the grind for em(for em). WhaServed that time for em(for em). Cant see ya did it for me, so i feel like i owe em. Now Tim Ridin with me, everybody tryna get me, till the day i die im livin filthy(filty).
    (chorus)
    Timbo- When you hit me on my phone betta know what cha want, when you call me, you already know, on the low, im sayin Hey! i got that(dro). I got that(drank). I got that(?). I got. I gotta pocket fulla stones and im playin the corner, you want it, you already know, you sicko. Im sayin Hey!.about that. Hey!.about that. Hey!.about that. Hey! about. whoo!
    (uh huh, uh huh, uh huh)
    (verse 2, Timbaland)
    Timbo- lemme tell ya bout this nigga name Tim(name Tim). Im well known in them corners V.A. to California, the game sowed up and you wanna blame him(blame him), and throw yo side up homie nd ill throw minez up homie, till i retire, Only GOD knows when(knows when :]) im Mr. Mo'endz, if you aint talkin paper i tell ya Go'on then. I gotta team of goons they kidnapping grown men, duct taping wife and kids, thinkin niggas gone then. An when i ride by, ima let them slugs fly, bustin my forty five, say hi to the bad guy. Yea, my swagg is stupid, my status celebrity, so i dont really gotta shoot cha you already dead to me.
    (chorus)
    Timbo- When you hit me on my phone betta know what cha want, when you call me, you already know, on the low, im sayin Hey! i got that(dro). I got that(drank). I got that(?). I got. I gotta pocket fulla stones and im playin the corner, you want it, you already know, you sicko. Im sayin Hey!.about that. Hey!.about that. Hey!.about that. Hey! about. whoo!
    (verse 3)
    Lil Eazy E- and i aint stoppin for nothin, cant get enough of it. This dope game such a rush and a nigga lovin it. Fast money,Fast cars im on some other- (Timbaland)|

    """

    partial_matched_lyrics = get_partial_match_substring(sample_lyrics.lower(),given_word)

    assert  partial_matched_lyrics == "nd ill throw minez up homie, till i retire, only god knows when(knows when :]) im mr. mo'endz, if you"



def test_get_top_sample_lyrics():

    """
    Test getting 10 songs which the lyrics contains "peace"

    """

    given_word = "peace"

    song_data = get_top_sample_lyrics(given_word)

    assert len(song_data) == 10

    print(song_data)

def test_get_one_song():

    """
    Test gee return one song with given artist name and song title

    """

    given_artist = "drake"
    given_song_title = "best-i-ever-had-remix"

    song_data = get_one_song(given_artist,given_song_title)

    assert song_data['artist'] == given_artist
    assert song_data['song'] == given_song_title


def test_get_one_song_by_id():

    """
    Test gee return one song with given song id

    """

    given_song_id = 24851
    given_artist = "Heng"
    given_song_title = "I can do all things (Remix)"

    song_data = get_one_song_by_id(given_song_id)

    assert song_data['artist'] == given_artist
    assert song_data['song'] == given_song_title



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

    assert  make_response == "The song title I can do all things is deleted for artist: Heng."







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

