#!/usr/bin/env python

import wof
import wof.flask

from wof.examples.flask.piabanha.piabanha_dao import OdmDao

"""
    python examples/flask/piabanha/runserver_piabanha.py private.connection --config=examples/piabanha/config.cfg
    where private.connection is a file that has connection string: postgresql+psycopg2://postgres:postgres@localhost:5432/odm_piabanha

"""


connection_file = open('postgresql.conn', 'r')
config = 'config.cfg'
dao = OdmDao(connection_file.read())
app = wof.flask.create_wof_flask_app(dao, config)

