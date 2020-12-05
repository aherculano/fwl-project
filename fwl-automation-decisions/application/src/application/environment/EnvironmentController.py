from domain.model.environment import EnvironmentRepository
from .EnvironmentDTO import EnvironmentDTO
from .EnvironmentMapper import EnvironmentMapper


class EnvironmentController(object):

    def __init__(self, mapper: EnvironmentMapper, repo: EnvironmentRepository):
        self.mapper = mapper
        self.repo = repo

    def list(self) -> [EnvironmentDTO]:
        dom_list = self.repo.list()
        ret_list: [EnvironmentDTO] = []
        for dom in dom_list:
            ret_list.append(self.mapper.domain2dto(dom))
        return ret_list

    def add(self, dto: EnvironmentDTO):
        dom = self.mapper.dto2domain(dto)
        self.repo.add(dom)
        return self.mapper.domain2dto(dom)
