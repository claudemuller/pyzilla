#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Decode Filezilla locally stored passwords from sitemanager.xml

author: Claude Müller
website: http://unschooled.life

"""

import sys
import base64
from xml.dom.minidom import parse

# Print usage
if len(sys.argv) < 2:
    print('usage: %s <sitemanager.xml>' % sys.argv[0]);
    sys.exit(1)

# Parse the sitemanager.xml file
doc = parse(sys.argv[1])

# Loop over Server keys
for server in doc.getElementsByTagName('Server'):
    for pword in server.getElementsByTagName('Host'):
        print('Host:\t\t%s' % pword.firstChild.nodeValue)

    for pword in server.getElementsByTagName('Pass'):
        # base64 decode the password before printing
        print('Password:\t%s\n' % base64.b64decode(pword.firstChild.nodeValue))

