from flask import Flask, redirect, url_for, request, make_response
from view_funcs.funcs import *

class EndpointHandler:

    def __init__(self, action):
        self.action = action 

    def __call__(self, *args, **kwargs):
        response = self.action(*args, **request.view_args)
        return make_response(response)

class FlaskAppWraper:

    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def setUrl(self, rule=None, endpoint=None, view_func=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(rule, endpoint, EndpointHandler(view_func), methods=methods, *args, **kwargs)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

if __name__ == "__main__":
    app = FlaskAppWraper(Flask(__name__))
    app.setUrl('/', 'mainPage', mainPage)
    app.run(debug=True)