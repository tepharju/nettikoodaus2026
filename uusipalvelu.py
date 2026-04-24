from wsgiref.simple_server import make_server

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "Hello World!".encode('utf-8')
    yield "<p>".encode('utf-8')
    
    yield """<form enctype="application/x-www-urlencoded">""".encode('utf-8')
    yield """<input name=kysely type=text value="Kirjoita tähän jotain">""".encode('utf-8')
    yield "</form>".encode('utf-8')
    
    yield "<p>".encode('utf-8')
    
    for key in environ:
        yield ("%s: %s\n" % (key, environ[key])).encode('utf-8')
    
if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server:
        server.serve_forever()
        
        
