__author__ = 'h_hack'

from firebase import firebase
from config import FirebaseURL

"""json_dict = {}

json_dict['TextMessage']= 'keep contributing because it is fun and peaceful.'
json_dict['ImagePath'] = 'https://scontent.fmaa1-2.fna.fbcdn.net/v/t1.0-0/s526x395/12509001_1317294144954125_841824305318638405' \
                '3_n.jpg?oh=28a153a33e1471d1a0707e2308519051&oe=57EBBEED'
json_dict['LinkPath'] = 'https://www.saavishkaar.in'
"""

def FirebasePost(data):
    myfirebase = firebase.FirebaseApplication(FirebaseURL)
    myfirebase.post('/data', data=data, params={'print': 'pretty'})


def FirebaseGet():
    myfirebase = firebase.FirebaseApplication(FirebaseURL)
    data = myfirebase.get('/data', None, params={'print': 'pretty'})
    return data