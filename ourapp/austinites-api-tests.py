#!/usr/bin/env python3.3
"""
Test cases for the Austinites API. Each API call tests for the response
code, content-type, and dictionary content posted in The Austin City Limits
Project API.
"""

from unittest import TestCase, main
import requests
from random import randint

class APICallTests(TestCase) :

    #/api/stages/

    stages = requests.get('http://theaustinites.pythonanywhere.com/api/stages/')
    stages_json = stages.json()
    stages_length = len(stages_json)

    def test_stages_1(self) :
        self.assertEqual(self.stages.status_code, 200)

    def test_stages_2(self) :
         self.assertEqual(self.stages.headers['content-type'], 'application/json')

    def test_stages_3(self) :
         self.assertEqual([ ('location' in d) for d in self.stages_json], [True] * self.stages_length)

    def test_stages_4(self) :
         self.assertEqual([ (type(d['location']) is int) for d in self.stages_json if ('location' in d) ], [True] * self.stages_length)

    def test_stages_5(self) :
         self.assertEqual([ ('years' in d) for d in self.stages_json], [True] * self.stages_length)

    def test_stages_6(self) :
         self.assertEqual([ (type(d['years']) is list) for d in self.stages_json if ('years' in d) ], [True] * self.stages_length)


    #/api/stages/{location}/

    stage_id = randint(1, stages_length)
    stage = requests.get('http://theaustinites.pythonanywhere.com/api/stages/' + str(stage_id))
    stage_json = stage.json()

    def test_stage_1(self) :
        self.assertEqual(self.stage.status_code, 200)

    def test_stage_2(self) :
         self.assertEqual(self.stage.headers['content-type'], 'application/json')

    def test_stage_3(self) :
         self.assertEqual( 'location' in self.stage_json, True)

    def test_stage_4(self) :
         self.assertEqual( 'location' in self.stage_json and type(self.stage_json['location']) is int, True)

    def test_stage_5(self) :
         self.assertEqual( 'years' in self.stage_json, True)

    def test_stage_6(self) :
         self.assertEqual( 'years' in self.stage_json and type(self.stage_json['years']) is list, True)

    #/api/stages/{location}/media

    stage_id = randint(1, 8)
    stage_media = requests.get('http://theaustinites.pythonanywhere.com/api/stages/' + str(stage_id) + '/media/')
    stage_media_json = stage_media.json()

    def test_stage_media_1(self) :
        self.assertEqual(self.stage_media.status_code, 200)

    def test_stage_media_2(self) :
         self.assertEqual(self.stage_media.headers['content-type'], 'application/json')

    def test_stage_media_3(self) :
         self.assertEqual( 'location' in self.stage_media_json, True)

    def test_stage_media_4(self) :
         self.assertEqual( 'location' in self.stage_media_json and type(self.stage_media_json['location']) is int, True)

    def test_stage_media_5(self) :
         self.assertEqual( 'bio' in self.stage_media_json, True)

    def test_stage_media_6(self) :
         self.assertEqual( 'bio' in self.stage_media_json and type(self.stage_media_json['bio']) is str, True)

    def test_stage_media_7(self) :
         self.assertEqual( 'photo' in self.stage_media_json, True)

    def test_stage_media_8(self) :
         self.assertEqual( 'photo' in self.stage_media_json and type(self.stage_media_json['photo']) is str, True)

    def test_stage_media_9(self) :
         self.assertEqual( 'youtube' in self.stage_media_json, True)

    def test_stage_media_10(self) :
         self.assertEqual( 'youtube' in self.stage_media_json and type(self.stage_media_json['youtube']) is str, True)

    def test_stage_media_11(self) :
         self.assertEqual( 'video' in self.stage_media_json, True)

    def test_stage_media_12(self) :
         self.assertEqual( 'video' in self.stage_media_json and type(self.stage_media_json['video']) is str, True)

    def test_stage_media_13(self) :
         self.assertEqual( 'twitter' in self.stage_media_json, True)

    def test_stage_media_14(self) :
         self.assertEqual( 'twitter' in self.stage_media_json and type(self.stage_media_json['twitter']) is str, True)

    def test_stage_media_15(self) :
         self.assertEqual( 'twitterwidget' in self.stage_media_json, True)

    def test_stage_media_16(self) :
         self.assertEqual( 'twitterwidget' in self.stage_media_json and type(self.stage_media_json['twitterwidget']) is str, True)

    def test_stage_media_17(self) :
         self.assertEqual( 'webpage' in self.stage_media_json, True)

    def test_stage_media_18(self) :
         self.assertEqual( 'webpage' in self.stage_media_json and type(self.stage_media_json['webpage']) is str, True)

    def test_stage_media_19(self) :
         self.assertEqual( 'name' in self.stage_media_json, True)

    def test_stage_media_20(self) :
         self.assertEqual( 'name' in self.stage_media_json and type(self.stage_media_json['name']) is str, True)

    def test_stage_media_21(self) :
         self.assertEqual( 'facebook' in self.stage_media_json, True)

    def test_stage_media_22(self) :
         self.assertEqual( 'facebook' in self.stage_media_json and type(self.stage_media_json['facebook']) is str, True)

    def test_stage_media_23(self) :
         self.assertEqual( 'year' in self.stage_media_json, True)

    def test_stage_media_24(self) :
         self.assertEqual( 'year' in self.stage_media_json and type(self.stage_media_json['year']) is int, True)

    #/api/sponsors

    sponsors = requests.get('http://theaustinites.pythonanywhere.com/api/sponsors/')
    sponsors_json = sponsors.json()
    sponsors_length = len(sponsors_json)

    def test_sponsors_1(self) :
        self.assertEqual(self.sponsors.status_code, 200)

    def test_sponsors_2(self) :
         self.assertEqual(self.sponsors.headers['content-type'], 'application/json')

    def test_sponsors_3(self) :
         self.assertEqual([ ('id' in d) for d in self.sponsors_json], [True] * self.sponsors_length)

    def test_sponsors_4(self) :
         self.assertEqual([ (type(d['id']) is int) for d in self.sponsors_json if ('id' in d) ], [True] * self.sponsors_length)

    def test_sponsors_5(self) :
         self.assertEqual([ ('name' in d) for d in self.sponsors_json], [True] * self.sponsors_length)

    def test_sponsors_6(self) :
         self.assertEqual([ (type(d['name']) is str) for d in self.sponsors_json if ('name' in d) ], [True] * self.sponsors_length)

    def test_sponsors_7(self) :
         self.assertEqual([ ('industry' in d) for d in self.sponsors_json], [True] * self.sponsors_length)

    def test_sponsors_8(self) :
         self.assertEqual([ (type(d['industry']) is str) for d in self.sponsors_json if ('industry' in d) ], [True] * self.sponsors_length)

    def test_sponsors_9(self) :
         self.assertEqual([ ('years' in d) for d in self.sponsors_json], [True] * self.sponsors_length)

    def test_sponsors_10(self) :
         self.assertEqual([ (type(d['years']) is list) for d in self.sponsors_json if ('years' in d) ], [True] * self.sponsors_length)

    def test_sponsors_11(self) :
         self.assertEqual([ ('stage_locations' in d) for d in self.sponsors_json], [True] * self.sponsors_length)

    def test_sponsors_12(self) :
         self.assertEqual([ (type(d['stage_locations']) is list) for d in self.sponsors_json if ('stage_locations' in d) ], [True] * self.sponsors_length)

    #/api/sponsor/{id}

    sponsor_id = randint(13, 25)
    sponsor = requests.get('http://theaustinites.pythonanywhere.com/api/sponsors/' + str(sponsor_id))
    sponsor_json = sponsor.json()

    def test_sponsor_1(self) :
        self.assertEqual(self.sponsor.status_code, 200)

    def test_sponsor_2(self) :
         self.assertEqual(self.sponsor.headers['content-type'], 'application/json')

    def test_sponsor_3(self) :
         self.assertEqual( 'id' in self.sponsor_json, True)

    def test_sponsor_4(self) :
         self.assertEqual( 'id' in self.sponsor_json and type(self.sponsor_json['id']) is int, True)

    def test_sponsor_5(self) :
         self.assertEqual( 'name' in self.sponsor_json, True)

    def test_sponsor_6(self) :
         self.assertEqual( 'name' in self.sponsor_json and type(self.sponsor_json['name']) is str, True)

    def test_sponsor_7(self) :
         self.assertEqual( 'industry' in self.sponsor_json, True)

    def test_sponsor_8(self) :
         self.assertEqual( 'industry' in self.sponsor_json and type(self.sponsor_json['industry']) is str, True)

    def test_sponsor_9(self) :
         self.assertEqual( 'years' in self.sponsor_json, True)

    def test_sponsor_10(self) :
         self.assertEqual( 'years' in self.sponsor_json and type(self.sponsor_json['years']) is list, True)

    def test_sponsor_11(self) :
         self.assertEqual( 'stage_locations' in self.sponsor_json, True)

    def test_sponsor_12(self) :
         self.assertEqual( 'stage_locations' in self.sponsor_json and type(self.sponsor_json['stage_locations']) is list, True)

    #/api/sponsors/{id}/media

    sponsor_id = randint(13, 25)
    sponsor_media = requests.get('http://theaustinites.pythonanywhere.com/api/sponsors/' + str(sponsor_id) + '/media/')
    sponsor_media_json = sponsor_media.json()

    def test_sponsor_media_1(self) :
        self.assertEqual(self.sponsor_media.status_code, 200)

    def test_sponsor_media_2(self) :
         self.assertEqual(self.sponsor_media.headers['content-type'], 'application/json')

    def test_sponsor_media_3(self) :
         self.assertEqual( 'sponsor' in self.sponsor_media_json, True)

    def test_sponsor_media_4(self) :
         self.assertEqual( 'sponsor' in self.sponsor_media_json and type(self.sponsor_media_json['sponsor']) is int, True)

    def test_sponsor_media_5(self) :
         self.assertEqual( 'bio' in self.sponsor_media_json, True)

    def test_sponsor_media_6(self) :
         self.assertEqual( 'bio' in self.sponsor_media_json and type(self.sponsor_media_json['bio']) is str, True)

    def test_sponsor_media_7(self) :
         self.assertEqual( 'photo' in self.sponsor_media_json, True)

    def test_sponsor_media_8(self) :
         self.assertEqual( 'photo' in self.sponsor_media_json and type(self.sponsor_media_json['photo']) is str, True)

    def test_sponsor_media_9(self) :
         self.assertEqual( 'youtube' in self.sponsor_media_json, True)

    def test_sponsor_media_10(self) :
         self.assertEqual( 'youtube' in self.sponsor_media_json and type(self.sponsor_media_json['youtube']) is str, True)

    def test_sponsor_media_11(self) :
         self.assertEqual( 'video' in self.sponsor_media_json, True)

    def test_sponsor_media_12(self) :
         self.assertEqual( 'video' in self.sponsor_media_json and type(self.sponsor_media_json['video']) is str, True)

    def test_sponsor_media_13(self) :
         self.assertEqual( 'twitter' in self.sponsor_media_json, True)

    def test_sponsor_media_14(self) :
         self.assertEqual( 'twitter' in self.sponsor_media_json and type(self.sponsor_media_json['twitter']) is str, True)

    def test_sponsor_media_15(self) :
         self.assertEqual( 'twitterwidget' in self.sponsor_media_json, True)

    def test_sponsor_media_16(self) :
         self.assertEqual( 'twitterwidget' in self.sponsor_media_json and type(self.sponsor_media_json['twitterwidget']) is str, True)

    def test_sponsor_media_17(self) :
         self.assertEqual( 'webpage' in self.sponsor_media_json, True)

    def test_sponsor_media_18(self) :
         self.assertEqual( 'webpage' in self.sponsor_media_json and type(self.sponsor_media_json['webpage']) is str, True)

    def test_sponsor_media_19(self) :
         self.assertEqual( 'facebook' in self.sponsor_media_json, True)

    def test_sponsor_media_20(self) :
         self.assertEqual( 'facebook' in self.sponsor_media_json and type(self.sponsor_media_json['facebook']) is str, True)

    #/api/artists

    artists = requests.get('http://theaustinites.pythonanywhere.com/api/artists/')
    artists_json = artists.json()
    artists_length = len(artists_json)

    def test_artists_1(self) :
        self.assertEqual(self.artists.status_code, 200)

    def test_artists_(self) :
         self.assertEqual(self.artists.headers['content-type'], 'application/json')

    def test_artists_3(self) :
         self.assertEqual([ ('id' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_4(self) :
         self.assertEqual([ (type(d['id']) is int) for d in self.artists_json if ('id' in d) ], [True] * self.artists_length)

    def test_artists_5(self) :
         self.assertEqual([ ('name' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_6(self) :
         self.assertEqual([ (type(d['name']) is str) for d in self.artists_json if ('name' in d) ], [True] * self.artists_length)

    def test_artists_7(self) :
         self.assertEqual([ ('label' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_8(self) :
         self.assertEqual([ (type(d['label']) is str) for d in self.artists_json if ('label' in d) ], [True] * self.artists_length)

    def test_artists_9(self) :
         self.assertEqual([ ('origin' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_10(self) :
         self.assertEqual([ (type(d['origin']) is str) for d in self.artists_json if ('origin' in d) ], [True] * self.artists_length)

    def test_artists_11(self) :
         self.assertEqual([ ('stage_locations' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_12(self) :
         self.assertEqual([ (type(d['stage_locations']) is list) for d in self.artists_json if ('stage_locations' in d) ], [True] * self.artists_length)

    def test_artists_13(self) :
         self.assertEqual([ ('genre' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_14(self) :
         self.assertEqual([ (type(d['genre']) is str) for d in self.artists_json if ('genre' in d) ], [True] * self.artists_length)

    def test_artists_15(self) :
         self.assertEqual([ ('years' in d) for d in self.artists_json], [True] * self.artists_length)

    def test_artists_16(self) :
         self.assertEqual([ (type(d['years']) is list) for d in self.artists_json if ('years' in d) ], [True] * self.artists_length)

    #/api/artists/{id}

    artist_id = randint(74, 92)
    artist = requests.get('http://theaustinites.pythonanywhere.com/api/artists/' + str(artist_id))
    artist_json = artist.json()

    def test_artist_1(self) :
        self.assertEqual(self.artist.status_code, 200)

    def test_artist_2(self) :
         self.assertEqual(self.artist.headers['content-type'], 'application/json')

    def test_artist_3(self) :
         self.assertEqual( 'id' in self.artist_json, True)

    def test_artist_4(self) :
         self.assertEqual( 'id' in self.artist_json and type(self.artist_json['id']) is int, True)

    def test_artist_5(self) :
         self.assertEqual( 'name' in self.artist_json, True)

    def test_artist_6(self) :
         self.assertEqual( 'name' in self.artist_json and type(self.artist_json['name']) is str, True)

    def test_artist_7(self) :
         self.assertEqual( 'label' in self.artist_json, True)

    def test_artist_8(self) :
         self.assertEqual( 'label' in self.artist_json and type(self.artist_json['label']) is str, True)

    def test_artist_9(self) :
         self.assertEqual( 'origin' in self.artist_json, True)

    def test_artist_10(self) :
         self.assertEqual( 'origin' in self.artist_json and type(self.artist_json['origin']) is str, True)

    def test_artist_11(self) :
         self.assertEqual( 'stage_locations' in self.artist_json, True)

    def test_artist_12(self) :
         self.assertEqual( 'stage_locations' in self.artist_json and type(self.artist_json['stage_locations']) is list, True)

    def test_artist_13(self) :
         self.assertEqual( 'genre' in self.artist_json, True)

    def test_artist_14(self) :
         self.assertEqual( 'genre' in self.artist_json and type(self.artist_json['genre']) is str, True)

    def test_artist_15(self) :
         self.assertEqual( 'years' in self.artist_json, True)

    def test_artist_16(self) :
         self.assertEqual( 'years' in self.artist_json and type(self.artist_json['years']) is list, True)

    #/api/artists/{id}/media

    artist_id = randint(74, 92)
    artist_media = requests.get('http://theaustinites.pythonanywhere.com/api/artists/' + str(artist_id) + '/media/')
    artist_media_json = artist_media.json()

    def test_artist_media_1(self) :
        self.assertEqual(self.artist_media.status_code, 200)

    def test_artist_media_2(self) :
         self.assertEqual(self.artist_media.headers['content-type'], 'application/json')

    def test_artist_media_3(self) :
         self.assertEqual( 'artist' in self.artist_media_json, True)

    def test_artist_media_4(self) :
         self.assertEqual( 'artist' in self.artist_media_json and type(self.artist_media_json['artist']) is int, True)

    def test_artist_media_5(self) :
         self.assertEqual( 'bio' in self.artist_media_json, True)

    def test_artist_media_6(self) :
         self.assertEqual( 'bio' in self.artist_media_json and type(self.artist_media_json['bio']) is str, True)

    def test_artist_media_7(self) :
         self.assertEqual( 'photo' in self.artist_media_json, True)

    def test_artist_media_8(self) :
         self.assertEqual( 'photo' in self.artist_media_json and type(self.artist_media_json['photo']) is str, True)

    def test_artist_media_9(self) :
         self.assertEqual( 'youtube' in self.artist_media_json, True)

    def test_artist_media_10(self) :
         self.assertEqual( 'youtube' in self.artist_media_json and type(self.artist_media_json['youtube']) is str, True)

    def test_artist_media_11(self) :
         self.assertEqual( 'video' in self.artist_media_json, True)

    def test_artist_media_12(self) :
         self.assertEqual( 'video' in self.artist_media_json and type(self.artist_media_json['video']) is str, True)

    def test_artist_media_13(self) :
         self.assertEqual( 'twitter' in self.artist_media_json, True)

    def test_artist_media_14(self) :
         self.assertEqual( 'twitter' in self.artist_media_json and type(self.artist_media_json['twitter']) is str, True)

    def test_artist_media_15(self) :
         self.assertEqual( 'twitterwidget' in self.artist_media_json, True)

    def test_artist_media_16(self) :
         self.assertEqual( 'twitterwidget' in self.artist_media_json and type(self.artist_media_json['twitterwidget']) is str, True)

    def test_artist_media_17(self) :
         self.assertEqual( 'webpage' in self.artist_media_json, True)

    def test_artist_media_18(self) :
         self.assertEqual( 'webpage' in self.artist_media_json and type(self.artist_media_json['webpage']) is str, True)

    def test_artist_media_19(self) :
         self.assertEqual( 'facebook' in self.artist_media_json, True)

    def test_artist_media_20(self) :
         self.assertEqual( 'facebook' in self.artist_media_json and type(self.artist_media_json['facebook']) is str, True)

main()