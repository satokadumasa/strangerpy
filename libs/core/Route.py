# Class Route
# coding: utf-8
import logging
import datetime
import uuid
import os, sys
import inspect
import re
 
class Route:
    """Routeクラス"""
    def __init__(self):
        self.default_actions = ['index', 'show', 'create', 'edit', 'save', 'delete']
        self.routes = []

        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        self.logger.info('test-log-dayo')

    def setRoute(self, url, controller, action):

        self.routes.append({'url':url, 'controller':controller, 'action':action})

    def findRoute(self, url):
        for route in self.routes:
            if re.match(route['url'], url):
                return route

    def getDefaultRoute(self, controllers_path):
        files = os.listdir(controllers_path)

        for file in files:
            self.logger.info('files:' + str(files))
            if (os.path.isdir(file)):
                self.getDefaultRoute(controllers_path + file + '/')

            controller = file.replace('Controller.py', '/')
            for default_action in self.default_actions:
                url = '/sdada/asdas'
                self.routes.append({'url':url, 'controller':controller, 'action':default_action})
