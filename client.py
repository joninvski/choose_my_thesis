#!/usr/bin/env python

import urllib
import urllib2

url = 'http://localhost:8000'
post_dict = {'subjects' : 'wsn sensores',
             'years' : 2,
             'qi' : 3}

params = urllib.urlencode(post_dict)
post_req = urllib2.Request(url)
post_req.add_data(params)

response = urllib2.urlopen(post_req)
response_data = response.read()
response.close()

print response_data
