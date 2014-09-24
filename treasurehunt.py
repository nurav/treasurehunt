__author__ = 'The Joshis'

import urllib
import urllib2
import json

def __main__():

    order = int(raw_input('start correct_order?\n'))
    while True:
        data = {}
        place = raw_input('enter location\n')
        if(place == 'exit'):
            return
        location = fetch(place)
        is_question = raw_input('is question?\n')
        if(is_question == 'y'):
            question = raw_input('question?\n')
            data['correct_order'] = order
            data['question'] = question
            data['location'] = location
            order = order + 1
        else:
            data['correct_order'] = -1
            data['question'] = None
            data['location'] = location

        print(json.dumps(data))


def fetch(place) :
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    values = {'key' : 'AIzaSyCvxoKs-hj8VoAt45mswWiGuxBj0561SOg',
            'address' : place}
    data = urllib.urlencode(values)

    request = urllib2.urlopen(url + data)

    info = json.loads(request.read())
    return info['results'][0]['geometry']['location']

if __name__ == '__main__':
    __main__()

