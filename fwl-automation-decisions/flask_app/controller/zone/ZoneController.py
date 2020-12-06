from application.zone.ZoneController import ZoneController
from domain.model.environment import EnvironmentRepository
from domain.model.zone import ZoneRepository
from flask_restx import Resource, Namespace, fields
from flask_restx.reqparse import RequestParser
from injector import inject
from .ZoneMapperImpl import ZoneMapperImpl
from .ZoneDTOImpl import ZoneDTOImpl


def get_parser() -> RequestParser:
    parser = RequestParser()
    parser.add_argument("zone_name", required=True, type=str)
    parser.add_argument("environment_name", required=True, type=str)
    return parser


api = Namespace("Zone", description="Datacenter Zones Functionality")

model = api.model("Zone", {
    'zone_name': fields.String,
    'environment_name': fields.String
})


@api.route("/")
class ZoneListResource(Resource):
    @inject
    def __init__(self, zone_repo: ZoneRepository, env_repo: EnvironmentRepository, **kwargs):
        self.zone_controller = ZoneController(ZoneMapperImpl(), zone_repo, env_repo)
        super().__init__(**kwargs)

    @api.expect(model)
    @api.marshal_with(model)
    def post(self):
        dto = ZoneDTOImpl.from_dict(api.payload)
        self.zone_controller.add(dto)
        return dto

    @api.marshal_list_with(model)
    def get(self):
        return self.zone_controller.list()