from __future__ import (absolute_import, division, print_function)

import logging

import wof
import wof.flask
from wof.examples.flask.csv_server.csv_dao import CsvDao

"""
    python runserver_csv.py
    Will run the exact example

    python runserver_csv.py
    --config=csv_config.cfg
    --sites_file=sites.csv
    --values_file=data.csv

"""
CSV_CONFIG_FILE = 'csv_config.cfg'
SITES_FILE = 'sites.csv'
VALUES_FILE = 'data.csv'

logging.basicConfig(level=logging.DEBUG)

def startServer(config=CSV_CONFIG_FILE,
                sites_file=SITES_FILE,
                values_file=VALUES_FILE,
                openPort=8080):
    dao = CsvDao(sites_file, values_file)
    app = wof.flask.create_wof_flask_app(dao, config)
    app.config['DEBUG'] = True


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
    # This must be an available port on your computer.
    # For example, if 8080 is already being used, try another port such as
    # 5000 or 8081.
    import argparse

    parser = argparse.ArgumentParser(description='start WOF for an ODM1 database.')
    parser.add_argument('--config',
                       help='Configuration file', default=CSV_CONFIG_FILE)
    parser.add_argument('--sites_file',
                       help='csv file containing sites information',default=SITES_FILE)
    parser.add_argument('--values_file',
                       help='csv file containing values',default=VALUES_FILE)
    parser.add_argument('--port',
                       help='Open port for server."', default=8080, type=int)

    args = parser.parse_args()
    print(args)

    startServer(config=args.config,sites_file=args.sites_file,values_file=args.values_file,openPort=args.port)
