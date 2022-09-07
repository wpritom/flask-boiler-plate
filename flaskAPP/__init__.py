from flask import Flask
from .api.routes import api
from .web.routes import web

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(web, url_prefix="/web")