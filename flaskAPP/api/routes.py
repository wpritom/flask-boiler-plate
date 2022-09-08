from flask import Blueprint, request
from flask.views import MethodView

from flaskAPP.extension import send_response

#### NOTE: importing Dummy Database #########
from flaskAPP.extension import user_database
#############################################

api = Blueprint('api', __name__)

class Index(MethodView):
    init_every_request = False

    def get(self, value=None):
        return send_response("FlaskAPP API", data={"site_url": request.root_url})

class UserAPI(MethodView):
    init_every_request = False

    def get(self, value=None):
        print(value)
        # from dummy data
        if value==None:
            message = f"No User profile asked"
            return send_response(message)
        else:
            for user in user_database:
                if user['id'] == int(value):
                    return send_response("User Found",data={'username':user['username']})

            return send_response("User Not Found")
        


    def post(self):
        # new user creation
        print(request.form)


def register_view(app, url_prefix=None, method_view=None, name=None):
    app.add_url_rule(f'{url_prefix}/<value>', view_func = method_view.as_view(f"{name}_get"))
    app.add_url_rule(f'{url_prefix}/', view_func = method_view.as_view(f"{name}_post"))

register_view(api, '', Index, "Index")
register_view(api, 'user', UserAPI, "UserAPI")