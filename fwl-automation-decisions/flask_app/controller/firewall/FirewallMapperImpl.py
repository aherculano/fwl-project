from application.firewall.FirewallMapper import FirewallMapper
from domain.model.firewall import Firewall, FirewallAccessLayer, FirewallName, FirewallUUID
from .FirewallDTOImpl import FirewallDTOImpl


class FirewallMapperImpl(FirewallMapper):
    def dto2domain(self, dto: FirewallDTOImpl) -> Firewall:
        return Firewall(FirewallUUID(dto.uuid), FirewallName(dto.name), FirewallAccessLayer(dto.access_layer))

    def domain2dto(self, dom: Firewall) -> FirewallDTOImpl:
        return FirewallDTOImpl(dom.uuid.value, dom.name.value, dom.access_layer.value)
