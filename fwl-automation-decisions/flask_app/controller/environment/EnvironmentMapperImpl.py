from application import EnvironmentMapper
from domain.model.environment import Environment, EnvironmentName

from .EnvironmentDTOImpl import EnvironmentDTOImpl


class EnvironmentMapperImpl(EnvironmentMapper):
    def dto2domain(self, dto: EnvironmentDTOImpl) -> Environment:
        return Environment(EnvironmentName(dto.environment_name))

    def domain2dto(self, dom: Environment) -> EnvironmentDTOImpl:
        return EnvironmentDTOImpl(dom.environment_name.value)
