import pdb
import sys

from HTMLParser import HTMLParser

###############################
class GoogleScholarParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.counter = -2
        self.inside = False

    def handle_starttag(self, tag, attrs):
        if tag == "div" and attrs and attrs[0][0] == "id" and attrs[0][1] == 'gs_n': 
            self.inside = True

        if tag == "td" and self.inside:
            self.counter += 1

###############################

def crawl_google_schoolar(query):
    # ??? ver o que esta no ACM crawler
    print "Now going to crawl google schoolar"

    parser = GoogleScholarParser()
    url_string = 'http://scholar.google.pt/scholar?as_ylo=2013&hl=en&q='+query+'&btnG=&as_sdt=1%2C5&as_sdtp='
    # url_string = 'http://localhost:8001/page.html'

    import httplib
    httplib.HTTPConnection.debuglevel = 1                             

    import urllib2
    request = urllib2.Request(url_string) 
    opener = urllib2.build_opener()                                   
    request.add_header('User-Agent', 'OpenAnything/1.0 +http://diveintopython.org/')
    feeddata = opener.open(request).read()                            

    parser.feed(feeddata)

    return {'number_pages': parser.counter, 'average_year': 2007}

