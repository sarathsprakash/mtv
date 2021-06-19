import os
import json
from nameko.rpc import rpc
from session.utils import methods as _methods


class Session(object):
    name = "session"

    @_methods(['GET'])
    @rpc
    def docs(self):
        """ Gets Session service docs
        """
        path = "{}{}".format(os.getcwd(), '/session/docs/swagger.json')
        with open(path) as doc:
            return json.load(doc), 200