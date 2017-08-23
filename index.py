# index.py
# coding:utf-8
import logging
import datetime
import uuid
import os, sys
import cgi
import inspect

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
project_root = os.path.dirname(os.path.abspath(__file__))

sys.path.append(project_root)

import libs.core.Route

def main():
    # log
    logger.info('sys version' + str(sys.version_info))


def application(env, start_response):
    main()
    logger.info('project_root:' + project_root)
    print_char = ""
    
    print_char = getQuery(env)

    logger.info('print_char:' + print_char)
    url = env['REQUEST_URI']
    logger.info('url:' + url)
    
    r = Route()
    r.getDefaultRoute(project_root + '/app/controllers/')
    route = r.findRoute(url)
    logger.info("controller[" + route['controller'] + "] action[" + route['action'] + "]")

    start_response('200 OK', [('Content-type', 'text/html')])
    str = createView('index.tpl')
    return [str.encode("utf-8")]

def getQuery(env):
    print_char = ""

    method = env.get('REQUEST_METHOD')

    if method == 'GET':
        query = cgi.parse_qsl(env.get('QUERY_STRING'))
 
        for params in query:
            print_char += params[0] + ':' + params[1] + '<br>'

    if method == 'POST':
        wsgi_input = env['wsgi.input']
        content_length = int(env.get('CONTENT_LENGTH', 0))
        query = cgi.parse_qsl(wsgi_input.read(content_length))

        for params in query:
            print_char += params[0] + ':' + params[1] + '<br>'

    return print_char

def createView(file_name):
    arr = readTemplate(project_root + '/app/templates/' + file_name)
    str = ""

    for line in arr:
        str = str + line

    return str

def readTemplate(file_name):
    f = open(file_name, 'r')
    arr = []
    for line in f:
        arr.append(line)
    
    f.close()
    return arr