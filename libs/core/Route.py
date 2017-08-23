# Route.py
# coding: utf-8
import logging
import datetime
import uuid
import os, sys
import inspect
import re
 
class Route:
    """Routeクラス"""

    default_actions = ['index', 'show', 'create', 'edit', 'save', 'delete']

    def __init__(self):
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.info('test-log-dayo')

    def setRoute(url, controller, action):
        self.routes.apend({'url':url, 'controller':controller, 'action':action})

    def findRoute(url):
        for route in self.routes:
            if re.match(route['url'], url):
                return route

    def getDefaultRoute(controllers_path):
        files = os.listdir(controllers_path)

        for file in files:
            logger.info('files:' + files)
            if (is_dir(file)):
                self.getDefaultRoute(controllers_path + file + '/')

            controller = file.replace('Controller.py', '/')
            for default_action in self.default_actions:
                self.routes.apend({'url':url, 'controller':controller, 'action':default_action})
