from flask import Blueprint
from flask_restx import Api

from .environment.EnvironmentController import api as env_namespace

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="API")

api.add_namespace(env_namespace, "/api/environment")
