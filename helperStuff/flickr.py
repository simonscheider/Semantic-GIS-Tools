#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     04/10/2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import flickrapi
import json
import MySQLdb as mdb
import sys

#Simons key for flickr
xyz = "simon scheider"
api_key = u'153c6a19ad46be24d94f0c4dd791edb5'
api_secret = u'7f22e8b9f58c8a0b'

#This how to get flickr images in a geographic region with all data (location and time or for a specific user)
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
#photos = flickr.photos.search(user_id='73509078@N00', per_page='10')

#see: https://www.flickr.com/services/api/flickr.photos.search.html
hongkong = '113.887603, 22.215377, 114.360015, 22.51446'
photosinhk = flickr.photos.search(bbox=hongkong, has_geo=1,  per_page='10', extras='owner, date_taken, geo, tags, url_z', max_taken_date='2016-09-23 00:00:01', min_taken_date='2007-01-01 00:00:01')

#this turns the resut into a dict
parsed = json.loads(photosinhk.decode('utf-8'))

f = open("test.txt", "w")

f.write(str(parsed))



#print parsed
#this goes through the result and adds info from flickr
for i in parsed['photos']['photo']:
   # info=json.loads(flickr.photos.getInfo(photo_id=id).decode('utf-8'))
    id = i['id']
    #print i
    print id
    print i['title']
    print i['owner']
    print i['datetaken']
    print i['latitude']+' '+i['longitude']
    print i['tags']
    print i['url_z']
    #print i['date_create']
    #print flickr.photos.geo.getLocation(photo_id=id)
    #print info
    #print str(info['photo']['location']['latitude'])+' '+ str(info['photo']['location']['longitude'])
   # print str(info['photo']['dates']['taken'])




#The database connection: see http://zetcode.com/db/mysqlpython/
try:
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    db1 = MySQLdb.connect(host="localhost",user="root",passwd="****")
    cursor = db1.cursor()
    sql = 'CREATE DATABASE mydata'
    #cursor.execute(sql)


    sql = '''CREATE TABLE foo (
       bar VARCHAR(50) DEFAULT NULL
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1
       '''
    #cursor.execute(sql)

    ver = cur.fetchone()

    print "Database version : %s " % ver

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

#finally:
    #if con:
    #con.close()