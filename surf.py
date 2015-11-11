#!usr/bin/env python

import sys
import requests

def get_surf(spot_id):
    url = 'http://api.surfline.com/v1/forecasts/' + str(spot_id) + '?resources=analysis'
    request = requests.get(url)
    data = request.json()
    return data

spots = {
    'delmar': 4783,
    'blacks': 4245,
    'scripps': 4246,
    'ob': 4253,
    'sunsetcliffs': 4254,
    'missionbeach': 4252
}

def main(argv):
    if (len(argv) != 2):
        print "usage: surf <spot_name>"
        print "available spots: "
        for s in spots.keys():
            print s
    else:
        spot = argv[1]
        print u'\U0001F30A'
        try:
            data = get_surf(spots[spot])
            print data["Analysis"]["surfRange"][0]
            print data["Analysis"]["generalCondition"][0]
        except KeyError:
            print "No data for spot %s" % spot

if __name__ == '__main__':
    main(sys.argv)
