#-------------------------------------------------------------------------------
# Name:       try out allevents API
# Purpose:
#
# Author:      simon
#
# Created:     07/06/2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
    ########### Python 2.7 #############
import httplib, urllib, base64

def main():


    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '7eb8445d5b324934b9c83b74015297da',
    }

    params = urllib.urlencode({
        # Request parameters
        'query': 'concert',
        'latitude': '{string}',
        'longitude': '{string}',
        'city': 'Utrecht',
        'page': '1',
    })

    try:
        conn = httplib.HTTPSConnection('api.allevents.in')
        conn.request("POST", "/events/search/?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    main()
