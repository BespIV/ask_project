
def App( environ, start_response ):   

    status = "200 OK"

    headers = [
    ('Content-type', 'text/plain')
    ]

    if environ['QUERY_STRING'] != '':
        msg = "\n".join(environ.get('QUERY_STRING').split("&"))
    else:
        msg = ""

    start_response(status, headers)
    return [ msg ]