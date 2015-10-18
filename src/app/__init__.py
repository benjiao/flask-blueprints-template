from flask import Flask
from modules import default

app = Flask(__name__)
app.register_blueprint(default.mod)
