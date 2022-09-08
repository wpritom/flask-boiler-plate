from flask import Blueprint, request, session, render_template, url_for, redirect
from flask.views import MethodView
from flaskAPP.extension import send_response

import requests

web = Blueprint('web', __name__, template_folder='templates')

class Index(MethodView):
    init_every_request = False

    def get(self, value=None):
        return send_response(f"GET Request with value {value}")
    
    def post(self):
        return send_response(f"POST Request", data=dict(request.form))
    

class User(MethodView):
    init_every_request = False

    def get(self, value=None):
        # if 'username' in session:
        #     return render_template("user.html")
        data = requests.get(request.root_url + f'/api/{value}').json()
        
        return render_template("user.html")
    def post(self):
        # request.po
        # print(dict(request.form))
        # print(redirect(url_for('api.Index_post')))
        
        
        return render_template("user.html")

def register_view(app, url_prefix=None, method_view=None, name=None):
    print(f'{url_prefix}/<value>')
    app.add_url_rule(f'{url_prefix}/<value>', view_func = method_view.as_view(f"{name}_get"))
    app.add_url_rule(f'{url_prefix}/', view_func = method_view.as_view(f"{name}_post"))

register_view(web, '', Index, "Index")
register_view(web, 'user', User, "User")
