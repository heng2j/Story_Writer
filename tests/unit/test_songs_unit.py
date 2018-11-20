#!/usr/bin/env python3
# test_songs_unit.py
# ---------------
# Author: Zhongheng Li
# Start Date: 11-19-18
# Last Modified Date: 11-19-18


# System modules

# Internal modules
from songs import get_partial_match_substring, get_top_sample_lyrics, get_one_song


def test_partial_match_substring():
    """
    Test getting partial match Substring


    """

    given_phase = "know what"

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

    partial_matched_lyrics = get_partial_match_substring(sample_lyrics.lower(), given_phase)

    print('partial_matched_lyrics: ', partial_matched_lyrics)



    assert  given_phase in partial_matched_lyrics


def test_get_top_sample_lyrics():
    """
    Test getting 10 songs which the lyrics contains "peace"

    """

    given_word = "peace out"

    song_data = get_top_sample_lyrics(given_word)

    assert len(song_data) == 10

    # print(song_data)


def test_get_one_song():
    """
    Test gee return one song with given artist name and song title

    """

    given_artist = "drake"
    given_song_title = "best-i-ever-had-remix"

    song_data = get_one_song(given_artist, given_song_title)

    assert song_data['artist'] == given_artist
    assert song_data['song'] == given_song_title
