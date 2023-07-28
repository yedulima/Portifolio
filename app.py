from flask import Flask, request, make_response, template_rendered

class EndpointHandler:

    def __init__(self, action):
        self.action = action 

    def __call__(self, *args, **kwargs):
        response = self.action(*args, **request.view_args)
        return make_response(response)

class FlaskAppWrapper:

    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointHandler(handler), methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)

if __name__ == '__main__':
    app = FlaskAppWrapper(Flask(__name__))
    def action1():
        return '<h1>Hell World! Dawn</h1>'
    app.add_endpoint('/', 'action1', action1)
    app.run(debug=True)