from flask import Blueprint, request
from flask.views import MethodView

from flaskAPP.extension import send_response

api = Blueprint('api', __name__)

class Index(MethodView):
    init_every_request = False

    def get(self, id=None):
        return send_response("FlaskAPP API", data={"site_url": request.root_url})
    



def register_view(app, method_view, name):
    app.add_url_rule(f'/<id>', view_func = method_view.as_view(f"{name}_get"))
    app.add_url_rule(f'/', view_func = method_view.as_view(f"{name}_post"))

register_view(api, Index, "Index")