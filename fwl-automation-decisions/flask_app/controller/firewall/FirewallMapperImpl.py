from application.firewall.FirewallMapper import FirewallMapper
from domain.model.firewall import Firewall
from .FirewallDTOImpl import FirewallDTOImpl


class FirewallMapperImpl(FirewallMapper):
    def dto2domain(self, dto: FirewallDTOImpl) -> Firewall:
        return Firewall(dto.uuid, dto.name, dto.description)

    def domain2dto(self, dom: Firewall) -> FirewallDTOImpl:
        return FirewallDTOImpl(dom.uuid.value, dom.name.value, dom.access_layer.value)
