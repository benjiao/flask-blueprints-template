from flask import Blueprint
from flask import render_template

mod = Blueprint('default', __name__)


@mod.route('/')
def index():
    return render_template('default/index.html')
