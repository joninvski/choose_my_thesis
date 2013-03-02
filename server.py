import pdb
import BaseHTTPServer

import urlparse
import parser

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

        # parse parameters - Done
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
    print "Creating a new page with information " + str(information)
    return '<html><head></head><body>This is the new page. We have seen %d pages of year %d </body></html>' % (information['number_pages'], information['average_year'])


def fetch_information(parameters):
    """Receives the parameters, fetches the scholar web pages and returns the stats

    :parameters: dictionary with parameters containing
                'subjects'
                ...

    :returns: dictionary of information

    """
    # Creates the url for google scholar
    print "These are my parameters " + str(parameters)

    query = ""
    for subject in parameters['subjects']:
        query += subject
    
    # Performs the http get
    information = parser.crawl_google_schoolar(query)

    return information


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "CLOSING"
    http.server_close()
