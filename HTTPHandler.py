import cherrypy

main = None

class HTTPHandler(object):
    def index(self):
        return "Hello World"
    
    index.exposed = True

def Init():
    cherrypy.quickstart(HTTPHandler())
    