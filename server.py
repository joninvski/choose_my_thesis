import pdb
import BaseHTTPServer

import urlparse

HOST_NAME = 'localhost'
PORT = 8000

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_POST(s):
        # Extract and print the contents of the POST
        length = int(s.headers['Content-Length'])
        post_data = urlparse.parse_qs(s.rfile.read(length).decode('utf-8'))

        print "Passed parameters"
        for key, value in post_data.iteritems():
            print "%s=%s" % (key, value)

        s.send_response(200)
        s.send_header("Content-type", "text/html")

        # parse parameters
        parameters = parse_parameters(s.path)

        # fetch web pages for information
        information = fetch_information(parameters)

        # present new page
        new_page = create_new_page(information)

        s.wfile.write(new_page)
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")

        s.end_headers()

def parse_parameters(url):
    """Get's the parameters (from URL???)

    :url: @todo
    :returns: dictionary with parameters parsed

    """
    #parse(URL getting only the parameters)

    return {'subjects':['WSN', 'sensor networks'] }

def create_new_page(information):
    return '<html><head></head><body>This is the new page</body></html>'


def fetch_information(parameters):
    """Receives the parameters, fetches the scholar web pages and returns the stats

    :parameters: @todo
    :returns: @todo

    """
    # Creates the url for google scholar
    query = ""
    for subject in parameters['subjects']:
        query += subject
    
    # Performs the http get
    page = crawl_google_schoolar()

    # Parse the retrieved website
    information = parse_google_scholar_page(page)

def crawl_google_schoolar():
    # ??? ver o que esta no ACM crawler
    page = '<html><head> here be pages </head></html>' # This is what I crawled

    return page

def parse_google_scholar_page(page):
    #Do regular expression for fetching number pages
    return {'number_pages': 5, 'average_year': 2007}


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "CLOSING"
    http.server_close()
