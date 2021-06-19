""" Module for frontent routes
"""

import os
import traceback

from nameko.standalone.rpc import ClusterRpcProxy
from flask import request, jsonify
from frontend import app

#TODO take config from enviroment
CONFIG = {'AMQP_URI': "amqp://guest:guest@rabbit:5672"}

#TODO avoid code duplication

@app.route('/api/<string:service_name>/<string:method_name>', strict_slashes=False, methods=['GET'])
@app.route('/api/<string:service_name>/<string:method_name>/<path:path>', strict_slashes=False, methods=['GET'])
def api_get(service_name, method_name, path=''):
    """ Routes HTTP GET requests to RPC service calls
    """
    args = []
    path = path.strip()
    if path and path != '/':
        args.extend(os.path.normpath(path).split('/'))
    kwargs =  request.args.to_dict(flat=False)
    with ClusterRpcProxy(CONFIG) as rpc_proxy:
        service = getattr(rpc_proxy, service_name)
        service_method = getattr(service, method_name)
        #TODO: exceptions to be handeled better
        try:
            result, status_code = service_method(*args, __method__=request.method, **kwargs)
        except Exception  as e:
            return {'error': traceback.format_exc()}, 500
        return jsonify(result), status_code

@app.route('/api/<string:service_name>/<string:method_name>', strict_slashes=False, methods=['POST'])
@app.route('/api/<string:service_name>/<string:method_name>/<path:path>', methods=['POST'])
def api_post(service_name, method_name, path=''):
    """ Routes HTTP POST requests to RPC service calls.
        Accepts only content type `application/json`.
    """
    args = []
    kwargs = {}
    path = path.strip()
    if path and path != '/':
        args.extend(os.path.normpath(path).split('/'))
    if request.headers.get('Content-Type') == 'application/json':
        kwargs = request.json
    kwargs.update(__method__=request.method)
    with ClusterRpcProxy(CONFIG) as rpc_proxy:
        service = getattr(rpc_proxy, service_name)
        service_method = getattr(service, method_name)
        #TODO: exceptions to be handeled better
        try:
            result, status_code = service_method(*args, **kwargs)
        except Exception  as e:
            return {'error': traceback.format_exc()}, 500
        return jsonify(result), status_code
