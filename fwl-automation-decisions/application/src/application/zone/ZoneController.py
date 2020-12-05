from domain.model.environment import EnvironmentRepository
from domain.model.zone import ZoneRepository

from .ZoneMapper import ZoneMapper
from .ZoneDTO import ZoneDTO


class ZoneController(object):

    # TODO : EXTRACT ADD TO A DOMAIN SERVICE
    def __init__(self, mapper: ZoneMapper, zone_repo: ZoneRepository, env_repo: EnvironmentRepository):
        self.mapper = mapper
        self.zone_repo = zone_repo
        self.env_repo = env_repo

    def list(self) -> [ZoneDTO]:
        dom_list = self.zone_repo.list()
        ret_list: [ZoneDTO] = []
        for dom in dom_list:
            ret_list.append(self.mapper.domain2dto(dom))
        return ret_list

    def add(self, dto: ZoneDTO) -> ZoneDTO:
        dom = self.mapper.dto2domain(dto)
        self.zone_repo.add(dom)
        return dto
