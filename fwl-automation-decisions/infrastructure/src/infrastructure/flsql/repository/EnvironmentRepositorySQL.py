from domain.model.environment import EnvironmentRepository, Environment, EnvironmentName
from ..SQLAlchemyBase import SQLAlchemyBase
from ..model.EnvironmentModel import EnvironmentModel


class EnvironmentRepositorySQL(EnvironmentRepository):

    def __init__(self, base_repo: SQLAlchemyBase):
        self.base_repo = base_repo

    def add(self, o: Environment) -> Environment:
        model = self._domain_to_schema(o)
        self.base_repo.db.session.add(model)
        self.base_repo.db.session.commit()

    def list(self) -> [Environment]:
        model_list: [EnvironmentModel] = self.base_repo.db.session.query(EnvironmentModel).all()
        if model_list.__len__() > 0:
            ret_list = []
            for model in model_list:
                ret_list.append(self._schema_to_domain(model))
            return ret_list
        return []

    def get(self, o: Environment) -> Environment:
        pass

    def get_by_id(self, id: EnvironmentName) -> Environment:
        pass

    def _schema_to_domain(self, schema: EnvironmentModel) -> Environment:
        return Environment(EnvironmentName(schema.name))

    def _domain_to_schema(self, domain: Environment) -> EnvironmentModel:
        env_name: str = domain.environment_name.environment_name
        return EnvironmentModel(env_name)
