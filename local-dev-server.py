#!/usr/bin/python
import cherrypy
import data

## Server for local development which mimics the CGI setup.

class Dev(object):
    @cherrypy.expose()
    def index(self):
        return file('index.html').read()

    @cherrypy.expose(alias='data.cgi')
    @cherrypy.tools.response_headers(headers=[('Content-type', 'text/javascript')])
    def data(self):
        return data.get_data()

    @cherrypy.expose(alias='handler.js')
    @cherrypy.tools.response_headers(headers=[('Content-type', 'text/javascript')])
    def handler(self):
        return open('handler.js').read()


cherrypy.quickstart(Dev())
