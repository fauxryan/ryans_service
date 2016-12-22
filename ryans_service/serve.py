# -*- coding: utf-8 -*-
import os

import cherrypy
from cherrypy._cpnative_server import CPHTTPServer
import click

from ryans_service.app import create_app


@click.command()
@click.option('--env', help='CherryPy settings: production, staging, dev')
@click.option('--native', help='Use the native server, not the WSGI server',
              is_flag=True)
def run(env, native):
    """
    Start listening and serving applications on the address and port defining in
    the configuration.
    """
    create_app()

    conf = '/etc/ryans_service.conf'
    if not os.path.isfile(conf):
        conf = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                             '..', 'conf',
                                             'ryans_service.conf'))
    cherrypy.config.update(conf)

    if env in ['production', 'staging']:
        cherrypy.config.update({'environment': env})

    if native:
        cherrypy.server = CPHTTPServer(cherrypy.server)
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run()