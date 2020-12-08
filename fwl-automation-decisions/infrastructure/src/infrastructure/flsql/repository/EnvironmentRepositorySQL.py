from domain.model.environment import EnvironmentRepository, Environment, EnvironmentName
from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.EnvironmentModel import EnvironmentModel


class EnvironmentRepositorySQL(EnvironmentRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: Environment) -> Environment:
        schema = self._domain_to_schema(o)
        self.base_repo.add(schema)
        return self._schema_to_domain(schema)

    def list(self) -> [Environment]:
        model_list: [EnvironmentModel] = self.base_repo.list(EnvironmentModel)
        if model_list.__len__() > 0:
            ret_list = []
            for model in model_list:
                ret_list.append(self._schema_to_domain(model))
            return ret_list
        return []

    def get(self, o: Environment) -> Environment:
        return self.get_by_id(o.environment_name)

    def get_by_id(self, id: EnvironmentName) -> Environment:
        schema = self.base_repo.get_by_filter(EnvironmentModel, EnvironmentModel.name, id.value)
        return self._schema_to_domain(schema)

    def exists(self, id: EnvironmentName) -> bool:
        dom = self.get_by_id(id)
        if dom:
            return True
        return False

    def _schema_to_domain(self, schema: EnvironmentModel) -> Environment:
        return Environment(EnvironmentName(schema.name))

    def _domain_to_schema(self, domain: Environment) -> EnvironmentModel:
        env_name: str = domain.environment_name.value
        return EnvironmentModel(env_name)
