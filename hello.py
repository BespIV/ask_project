
def app( environ, start_response ):   

    status = "200 OK"

    headers = [
    ('Content-type', 'text/plain')
    ]

    if environ['QUERY_STRING'] != '':
        for line in environ["QUERY_STRING"].split("&"):
            msg = msg+line+"\n"
        
    else:
        msg = " "

    start_response(status, headers)
    return msg