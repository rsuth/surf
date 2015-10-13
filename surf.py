#!/usr/local/bin/python

import sys
import requests

def get_surf(spot_id):
    url = 'http://api.surfline.com/v1/forecasts/' + str(spot_id) + '?resources=analysis'
    request = requests.get(url)
    data = request.json()
    return data['Analysis']['surfRange'][0]

spots = {
    'delmar': 4783,
    'blacks': 4245,
    'scripps': 4246,
    'ob': 4253,
    'sunsetcliffs': 4254,
    'missionbeach': 4252
}

def main(argv):
    print get_surf(spots[argv[1]])

if __name__ == '__main__':
    main(sys.argv)
