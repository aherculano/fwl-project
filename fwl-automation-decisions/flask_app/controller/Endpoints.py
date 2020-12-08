from flask import Blueprint
from flask_restx import Api

from .environment.EnvironmentController import api as env_namespace
from .zone.ZoneController import api as zone_namespace
from .firewall.FirewallController import api as firewall_namespace

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="API")

api.add_namespace(env_namespace, "/api/environment")
api.add_namespace(zone_namespace, "/api/zone")
api.add_namespace(firewall_namespace, "/api/firewall")
