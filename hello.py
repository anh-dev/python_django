def app(environ, start_response):
   status = "200 OK"
   list = environ['QUERY_STRING'].split("&")
   body = ''
   for x in list:         
       body = body + x + "\n"
   response_headers = [
     ('Content-Type', 'text/plain'),
     ('Content-Length', len(body))
   
   ]
   start_repsonse(status, response_headers)
   return [body]
