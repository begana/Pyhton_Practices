import sys


def application(environ, start_response):
    status = '200 OK'
    output = u'sys.path = %s' % repr(sys.path)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output.encode('UTF-8')]
