from flask import Blueprint, request
from flask.views import MethodView
from flaskAPP.extension import send_response

web = Blueprint('web', __name__)

class Index(MethodView):
    init_every_request = False

    def get(self, value=None):
        return send_response(f"GET Request with value {value}")
    
    def post(self):
        return send_response(f"POST Request", data=dict(request.form))
    

class User(MethodView):
    init_every_request = False

    def get(self, value=None):
        pass

    def post(self):
        pass

def register_view(app, url_prefix=None, method_view=None, name=None):
    app.add_url_rule(f'{url_prefix}/<value>', view_func = method_view.as_view(f"{name}_get"))
    app.add_url_rule(f'{url_prefix}/', view_func = method_view.as_view(f"{name}_post"))

register_view(web,'', Index, "Index")
