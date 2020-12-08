from domain.model.firewall import FirewallRepository, FirewallUUID, Firewall, FirewallName, FirewallAccessLayer
from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.FirewallModel import FirewallModel


class FirewallRepositorySQL(FirewallRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: Firewall) -> Firewall:
        schema = self._domain_to_schema(o)
        self.base_repo.add(schema)
        return self._schema_to_domain(schema)

    def list(self) -> [Firewall]:
        schema_list = self.base_repo.list(FirewallModel)
        ret_list: [Firewall] = []
        for schema in schema_list:
            ret_list.append(self._schema_to_domain(schema))
        return ret_list

    def get(self, o: Firewall) -> Firewall:
        return self.get_by_id(o.uuid)

    def get_by_id(self, id: FirewallUUID) -> Firewall:
        schema = self.base_repo.get_by_filter(FirewallModel, FirewallModel.uuid, id.value)
        return self._schema_to_domain(schema)

    def exists(self, id: FirewallUUID) -> bool:
        dom = self.get_by_id(id)
        if dom:
            return True
        return False

    def _schema_to_domain(self, schema: FirewallModel) -> Firewall:
        return Firewall(FirewallUUID(schema.uuid), FirewallName(schema.name), FirewallAccessLayer(schema.access_layer))

    def _domain_to_schema(self, domain: Firewall) -> FirewallModel:
        return FirewallModel(domain.uuid.value, domain.name.value, domain.access_layer.value)
