from __future__ import unicode_literals
from os import path
import nose
from nose.tools import *

from tinytag import *

test_sample_folder = path.join(path.dirname(__file__), 'samples')
testfiles = {'vbri.mp3': {'track_total': None, 'length': 0.5224489795918368, 'album': 'I Can Walk On Water I Can Fly', 'year': '2007', 'title': 'I Can Walk On Water I Can Fly', 'artist': 'Basshunter', 'track': '01'},
             'cbr.mp3': {'track_total': None, 'length': 0.4963265306122449, 'album': 'I Can Walk On Water I Can Fly', 'year': '2007', 'title': 'I Can Walk On Water I Can Fly', 'artist': 'Basshunter', 'track': '01'},
             'id3v22-test.mp3': {'track_total': '11', 'length': 0.156734693877551, 'album': 'Hymns for the Exiled', 'year': '2004', 'title': 'cosmic american', 'artist': 'Anais Mitchell', 'track': '3'},
             'silence-44-s-v1.mp3': {'track_total': None, 'length': 3.7355102040816326, 'album': 'Quod Libet Test Data', 'year': '2004', 'title': 'Silence', 'artist': 'piman', 'track': '2'},
             'UTF16.mp3': {'length': 0.052244897959183675, 'track_total': '11', 'track': '07', 'artist': 'The National', 'year': '2010', 'album': 'High Violet', 'title': 'Lemonworld'},
             'empty.ogg': {'track_total': None, 'length': 3.684716553287982, 'album': None, '_max_samplenum': 162496, 'year': None, 'title': None, 'artist': None, 'track': None, '_tags_parsed': False},
             'multipagecomment.ogg': {'track_total': None, 'length': 3.684716553287982, 'album': None, '_max_samplenum': 162496, 'year': None, 'title': None, 'artist': None, 'track': None, '_tags_parsed': False},
             'multipage-setup.ogg': {'track_total': None, 'length': 4.128798185941043, 'album': 'Timeless', 'year': '2006', 'title': 'Burst', 'artist': 'UVERworld', 'track': '7', '_tags_parsed': False},
             'test.ogg': {'track_total': None, 'length': 1.0, 'album': 'the boss', 'year': '2006', 'title': 'the boss', 'artist': 'james brown', 'track': '1', '_tags_parsed': False},
             'test.wav': {'length': 1.0},
             'test3sMono.wav': {'length': 3.0},
             'test-tagged.wav': {'length': 1.0},
             
             'flac1sMono.flac': {'track_total': None, 'album': None, 'year': None, 'length': 1.0, 'title': None, 'track': None, 'artist': None},
             'flac1.5sStereo.flac': {'track_total': None, 'album': None, 'year': None, 'length': 1.4995238095238095, 'title': None, 'track': None, 'artist': None},
             'flac_application.flac': {'track_total': None, 'album': 'Belle and Sebastian Write About Love', 'year': '2010-10-11', 'length': 273.64, 'title': 'I Want the World to Stop', 'track': '4/11', 'artist': 'Belle and Sebastian'},
             'no-tags.flac': {'track_total': None, 'album': None, 'year': None, 'length': 3.684716553287982, 'title': None, 'track': None, 'artist': None},
             'variable-block.flac': {'track_total': None, 'album': 'Appleseed Original Soundtrack', 'year': '2004', 'length': 261.68, 'title': 'DIVE FOR YOU', 'track': '01', 'artist': 'Boom Boom Satellites'},
             'emptyfile.mp3': {'track_total': None, 'album': None, 'year': None, 'length': 0, 'title': None, 'track': None, 'artist': None},
             }


def get_info(testfile, expected):
    filename = path.join(test_sample_folder, testfile)
    print(filename)
    tag = TinyTag.get(filename)
    for key, value in expected.items():
        result = getattr(tag, key)
        fmt_string = 'field "%s": got %s (%s) expected %s (%s)!'
        fmt_values = (key, repr(result), type(result), repr(value), type(value))
        assert result == value, fmt_string % fmt_values
    print(tag)
    print('')


def test_generator():
    for testfile, expected in testfiles.items():
        yield get_info, testfile, expected

@raises(LookupError)
def test_unsupported_filetype():
    get_info(path.join(test_sample_folder, 'unsupported.filetype'), {})

if __name__ == '__main__':
    nose.runmodule()
