from domain.model.environment import EnvironmentName
from domain.model.zone import ZoneRepository, ZoneName, Zone
from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.ZoneModel import ZoneModel


class ZoneRepositorySQL(ZoneRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: Zone) -> Zone:
        schema = self._domain_to_schema(o)
        self.base_repo.add(schema)
        return self._schema_to_domain(schema)

    def list(self) -> [Zone]:
        schema_list = self.base_repo.list(ZoneModel)
        ret_list: [Zone] = []
        for schema in schema_list:
            ret_list.append(self._schema_to_domain(schema))
        return ret_list

    def get(self, o: Zone) -> Zone:
        return self.get_by_id(o.zone_name)

    def get_by_id(self, id: ZoneName) -> Zone:
        schema = self.base_repo.get_by_filter(ZoneModel, ZoneModel.name, id.value)
        return self._schema_to_domain(schema)

    def exists(self, id: ZoneName) -> bool:
        dom = self.get_by_id(id)
        if dom:
            return True
        return False

    def _domain_to_schema(self, domain: Zone) -> ZoneModel:
        return ZoneModel(domain.zone_name.value, 0)

    def _schema_to_domain(self, schema: ZoneModel) -> Zone:
        return Zone(ZoneName(schema.name), EnvironmentName(schema.environment.name))
