#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)

import logging

import wof
import wof.flask
from wof.core import WOFConfig

from wof.examples.flask.piabanha.piabanha_dao import OdmDao

"""
    python examples/flask/piabanha/runserver_piabanha.py private.connection --config=examples/piabanha/config.cfg
    where private.connection is a file that has connection string: postgresql+psycopg2://postgres:postgres@localhost:5432/odm_piabanha

"""

logging.basicConfig(level=logging.DEBUG)


def startServer(connection, config='config.cfg',openPort=8080):
    """given an open file on connection, read it to get a connection string to open the database and start up flask running WOF."""
    dao = OdmDao(connection.read())
    app = wof.flask.create_wof_flask_app(dao, config)


    configFile = WOFConfig(config)

    url = "http://127.0.0.1:" + str(openPort)
    print("----------------------------------------------------------------")
    print("Service endpoints")
    for path in wof.flask.site_map_flask_wsgi_mount(app):
        print("{}{}".format(url, path))

    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("HTML Access Service endpoints at ")
    for path in wof.site_map(app):
        print("{}{}".format(url, path))

    print("----------------------------------------------------------------")

    app.run(host='0.0.0.0', port=openPort, threaded=True)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='start WOF for an ODM1 database.')
    parser.add_argument('connection', type=argparse.FileType('r'),
                       help='The name of a file containing the Connection String eg: private.connection which has: mysql://username:password@localhost/database')
    parser.add_argument('--config', default="config.cfg",
                       help='Configuration file')
    parser.add_argument('--port',
                       help='Open port for server."', default=8080, type=int)
    args = parser.parse_args()
    print(args)

    startServer(connection=args.connection,config=args.config,openPort=args.port)

