from domain.model.environment import EnvironmentName
from domain.model.zone import ZoneRepository, ZoneName, Zone
from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.ZoneModel import ZoneModel
from ..model.EnvironmentModel import EnvironmentModel


class ZoneRepositorySQL(ZoneRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: Zone) -> Zone:
        model = self._domain_to_schema(o)
        env = self.base_repo.db.session.query(EnvironmentModel).filter(
            EnvironmentModel.name == o.environment.value).first()
        model.env_id = env.id
        self.base_repo.db.session.add(model)
        self.base_repo.db.session.commit()
        return o

    def list(self) -> [Zone]:
        schema_list = self.base_repo.db.session.query(ZoneModel).all()
        ret_list: [Zone] = []
        for schema in schema_list:
            ret_list.append(self._schema_to_domain(schema))
        return ret_list

    def get(self, o: Zone) -> Zone:
        pass

    def get_by_id(self, id: ZoneName) -> Zone:
        pass

    def _domain_to_schema(self, domain: Zone) -> ZoneModel:
        return ZoneModel(domain.zone_name.value, 0)

    def _schema_to_domain(self, schema: ZoneModel) -> Zone:
        return Zone(ZoneName(schema.name), EnvironmentName(schema.environment.name))
