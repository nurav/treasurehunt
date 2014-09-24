__author__ = 'The Joshis'

import urllib
import urllib2
import json


def __main__():
    try:
        file = open('question_data.txt')
        all_data = json.loads(file.read())

    except:
        print("first use")
        all_data = []
    file = open('question_data.txt', 'w+')
    order = int(raw_input('start correct_order?\n'))
    while True:
        data = {}
        place = raw_input('enter location\n')
        if (place == 'exit'):
            file.write(json.dumps(all_data))
            return
        location = fetch(place)
        if location == -1:
            print('invalid location')
            continue
        is_question = raw_input('is question?\n')
        data['name'] = place
        if (is_question == 'y'):
            question = raw_input('question?\n')
            data['correct_order'] = order
            data['question'] = question
            data['location'] = location
            order = order + 1
        else:
            data['correct_order'] = -1
            data['question'] = None
            data['location'] = location
        all_data.append(data)

        print(json.dumps(data))


def fetch(place):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    values = {'key': 'AIzaSyCvxoKs-hj8VoAt45mswWiGuxBj0561SOg',
              'address': place}
    data = urllib.urlencode(values)

    request = urllib2.urlopen(url + data)

    info = json.loads(request.read())

    try:
        return info['results'][0]['geometry']['location']
    except:
        return -1


if __name__ == '__main__':
    __main__()

