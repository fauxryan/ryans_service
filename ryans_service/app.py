# -*- coding: utf-8 -*-
import cherrypy
from cherrypy.process.wspbus import states

from ryans_service.swagger import spec


class Application:
    @cherrypy.expose
    def index(self):
        return "Hello world"

    @cherrypy.expose
    def health(self):
        if cherrypy.engine.state not in [states.STARTED]:
            raise cherrypy.HTTPError('503 Service Unavailable')

    @cherrypy.expose
    def status(self):
        return ""


class Swagger:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.trailing_slash(missing=False)
    def index(self):
        return spec.to_dict()


def create_app():
    """
    Mount the applications at the path where they will be served by
    the server.
    """
    cherrypy.tree.mount(Application(), '/')
    cherrypy.tree.mount(Swagger(), '/swagger')
