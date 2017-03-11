#!/usr/bin/env python

from livereload import Server, shell


server = Server()
server.watch('*.xml', shell('xml2rfc draft-iops-grow-bgp-session-culling.xml -o live/index.html --html'))
server.serve(root='live/')
