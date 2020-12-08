from domain.model.firewall import FirewallRepository
from domain.model.zone import ZoneRepository
from domain.model.zone_connection import ZoneConnectionRepository, ZoneConnection
from .ZoneConnectionMapper import ZoneConnectionMapper
from .ZoneConnectionDTO import ZoneConnectionDTO


class ZoneConnectionController(object):
    def __init__(self, zone_repo: ZoneRepository, firewall_repo: FirewallRepository,
                 conn_repo: ZoneConnectionRepository, mapper: ZoneConnectionMapper):
        self.zone_repo = zone_repo
        self.firewall_repo = firewall_repo
        self.conn_repo = conn_repo
        self.mapper = mapper

    # TODO VERIFICATION AND EXTRACT TO A SERVICE
    def add(self, dto: ZoneConnectionDTO) -> ZoneConnectionDTO:
        dom = self.mapper.dto2domain(dto)
        self.conn_repo.add(dom)
        return self.mapper.domain2dto(dom)

    def list(self) -> [ZoneConnectionDTO]:
        dom_list = self.conn_repo.list()
        ret_list: [ZoneConnection] = []
        for dom in dom_list:
            ret_list.append(self.mapper.domain2dto(dom))
        return ret_list
