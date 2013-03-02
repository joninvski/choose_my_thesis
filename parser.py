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
    url_string = 'http://scholar.google.pt/scholar?hl=en&q=teste&btnG=&as_sdt=1%2C5&as_sdtp='
    # url_string = 'http://localhost:8001/page.html'

    import urllib
    web_site = urllib.urlopen(url_string)
    parser.feed(web_site.read())

    return {'number_pages': parser.counter, 'average_year': 2007}

def parse_conference(conference_url):
    parser = ConferenceListParser()

    import urllib
    print conference_url
    web_site = urllib.urlopen(conference_url['link'])
    parser.feed(web_site.read())
