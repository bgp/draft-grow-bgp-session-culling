#!/usr/bin/env python

import os
from livereload import Server, shell


ROOT_DIR='live/'
if not os.path.exists(ROOT_DIR):
    os.mkdir(ROOT_DIR)
server = Server()
server.watch('*.xml', shell('xml2rfc draft-ietf-grow-bgp-session-culling.xml -o live/index.html --html'))
server.serve(root=ROOT_DIR)
