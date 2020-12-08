from application.firewall.FirewallController import FirewallController
from domain.model.firewall import FirewallRepository
from flask_restx import Namespace, fields, Resource
from flask_restx.reqparse import RequestParser
from .FirewallMapperImpl import FirewallMapperImpl
from .FirewallDTOImpl import FirewallDTOImpl
from injector import inject


def get_parser() -> RequestParser:
    parser = RequestParser()
    parser.add_argument("environment_name", required=True, type=str)
    return parser


api = Namespace("Firewall", description="Datacenter Firewall Functionality")

model = api.model("Firewall", {
    'uuid': fields.String,
    'name': fields.String,
    'access_layer': fields.String
})


@api.route("/")
class EnvironmentListController(Resource):

    @inject
    def __init__(self, base_repo: FirewallRepository, **kwargs):
        self.controller = FirewallController(base_repo, FirewallMapperImpl())
        super().__init__(**kwargs)

    @api.doc("LIST FIREWALL")
    @api.marshal_list_with(model)
    def get(self):
        return self.controller.list()

    @api.doc("CREATE A FIREWALL")
    @api.marshal_with(model)
    @api.expect(model)
    def post(self):
        dto = FirewallDTOImpl.from_dict(api.payload)
        ret = self.controller.add(dto)
        return ret
