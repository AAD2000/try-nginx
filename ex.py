import datetime

def application(environ, start_response):
    status = '200 OK'
    output = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]