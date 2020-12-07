from domain.model.firewall import FirewallRepository
from .FirewallMapper import FirewallMapper
from .FirewallDTO import FirewallDTO


class FirewallController(object):

    def __init__(self, repo: FirewallRepository, mapper: FirewallMapper):
        self.repo = repo
        self.mapper = mapper

    def add(self, dto: FirewallDTO) -> FirewallDTO:
        dom = self.mapper.dto2domain(dto)
        self.repo.add(dom)
        return self.mapper.domain2dto(dom)

    def list(self) -> [FirewallDTO]:
        ret_list: [FirewallDTO] = []
        dom_list = self.repo.list()
        for dom in dom_list:
            ret_list.append(self.mapper.domain2dto(dom))
        return ret_list
