from domain.model.firewall import FirewallUUID
from domain.model.zone_connection import ZoneConnectionRepository, ZonePair, ZoneConnection, AllowedPort, Criticality
from infrastructure.flsql.model import ZoneConnectionModel

from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.AllowedPortModel import AllowedPortModel
from ..model.ZoneModel import ZoneModel
from ..model.FirewallModel import FirewallModel


class ZoneConnectionRepositorySQL(ZoneConnectionRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: ZoneConnection) -> ZoneConnection:
        schema = self._domain_to_schema(o)
        source_id = self.base_repo.get_by_filter(ZoneModel, ZoneModel.name, o.zone_pair.source_zone.value).id
        destination_id = self.base_repo.get_by_filter(ZoneModel, ZoneModel.name, o.zone_pair.destination_zone.value).id
        firewall_id = self.base_repo.get_by_filter(FirewallModel, FirewallModel.uuid, o.firewall_uuid.value).id
        schema.source_id = source_id
        schema.destination_id = destination_id
        schema.firewall_id = firewall_id
        self.base_repo.add(schema)
        return self._schema_to_domain(schema)

    def list(self) -> [ZoneConnection]:
        schema_list = self.base_repo.list(ZoneConnectionModel)
        ret_list: [ZoneConnection] = []
        for model in schema_list:
            ret_list.append(self._schema_to_domain(model))
        return ret_list

    def get(self, o: ZoneConnection) -> ZoneConnection:
        return self.get_by_id(o.zone_pair)

    def get_by_id(self, id: ZonePair) -> ZoneConnection:
        schema = self.base_repo.get_by_filter(ZoneConnectionModel, ZoneConnectionModel.uuid, id.get_pair_name())
        return self._schema_to_domain(schema)

    def exists(self, id: ZonePair) -> bool:
        if self.get_by_id(id):
            return True
        return False

    # TODO: REFACTOR THIS
    def _domain_to_schema(self, dom: ZoneConnection) -> ZoneConnectionModel:
        allowed_ports = []
        for port in dom.allowed_ports_list:
            schema = AllowedPortModel(port.value)
            allowed_ports.append(schema)
        return ZoneConnectionModel(None, None, None, dom.criticality.value, dom.zone_pair.get_pair_name(),
                                   allowed_ports)

    def _schema_to_domain(self, schema: ZoneConnectionModel) -> ZoneConnection:
        allowed_ports_list = []
        for port in schema.allowed_ports:
            allowed_ports_list.append(AllowedPort(port.port))
        conn = ZoneConnection(ZonePair(schema.source_zone.zone_name,
                                       schema.destination_zone.zone_name),
                              Criticality(schema.criticality),
                              FirewallUUID(schema.firewall.uuid),
                              allowed_ports_list)
        return conn
