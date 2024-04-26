from flask import Blueprint

app_bp = Blueprint('app_bp', __name__, url_prefix='/api')
from USER import *
from REVIEW import *
from SERVICE import *
from TASK import *
from TOWN import *
from USERSERVICEASSOC import *
