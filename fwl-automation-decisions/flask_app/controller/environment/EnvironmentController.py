from application import EnvironmentController
from domain.model.environment import EnvironmentRepository
from flask_restx import Namespace, fields, Resource
from flask_restx.reqparse import RequestParser

from .EnvironmentMapperImpl import EnvironmentMapperImpl

from .EnvironmentDTOImpl import EnvironmentDTOImpl
from injector import inject


def get_parser() -> RequestParser:
    parser = RequestParser()
    parser.add_argument("environment_name", required=True, type=str)
    return parser


api = Namespace("Environment", description="Datacenter Environment Functionality")

model = api.model("Environment", {
    'environment_name': fields.String
})


@api.route("/")
class EnvironmentListController(Resource):

    @inject
    def __init__(self, base_repo: EnvironmentRepository, **kwargs):
        self.controller = EnvironmentController(EnvironmentMapperImpl(), base_repo)
        super().__init__(**kwargs)

    @api.doc("LIST ENVIRONMENT")
    @api.marshal_list_with(model)
    def get(self):
        return self.controller.list()

    @api.doc("CREATE AN ENVIRONMENT")
    @api.marshal_with(model)
    @api.expect(model)
    def post(self):
        dto = EnvironmentDTOImpl.from_dict(api.payload)
        ret = self.controller.add(dto)
        return ret
