from flask import Blueprint, request
from flask.views import MethodView


web = Blueprint('web', __name__)

# @web.route("/")
# def index():
#     return {"msg": "this is web"}


class Index(MethodView):
    init_every_request = False

    def get(self, id=None):
        return {"msg" : f"GET Request with value {id}", "url":request.url_root}
    
    def post(self):
        return {"msg" : f"POST Request", "data": dict(request.form)}
    


# def register_api(app, model, url):
#     item = ItemAPI.as_view(f"{name}-item", model)
#     group = GroupAPI.as_view(f"{name}-group", model)
#     app.add_url_rule(f"/{name}/<int:id>", view_func=item)
#     app.add_url_rule(f"/{name}/", view_func=group)

def register_view(app, method_view, name):
    app.add_url_rule(f'/<id>', view_func = method_view.as_view(f"{name}_get"))
    app.add_url_rule(f'/', view_func = method_view.as_view(f"{name}_post"))

register_view(web, Index, "Index")
# web.add_url_rule('/<id>', view_func=Index.as_view("web_post"))
# web.add_url_rule('/', view_func=Index.as_view("web"))