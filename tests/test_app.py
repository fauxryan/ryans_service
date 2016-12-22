# -*- coding: utf-8 -*-
import json

from cherrypy.test import helper

from ryans_service.app import create_app


class ApplicationTest(helper.CPWebCase):

    @staticmethod
    def setup_server():
        create_app()

    def test_application_index(self):
        self.getPage('/')
        self.assertStatus('200 OK')
        self.assertBody(b'Hello world')

    def test_application_index(self):
        self.getPage('/swagger')
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'application/json')

        self.assertIsInstance(json.loads(self.body.decode('utf-8')), dict)
