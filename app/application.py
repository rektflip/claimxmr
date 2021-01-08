import cherrypy
from app import REST


class Application_cl(object):
    def __init__(self, path):
        self.path = path
        self.claim = REST.REST_cl(self.path)
