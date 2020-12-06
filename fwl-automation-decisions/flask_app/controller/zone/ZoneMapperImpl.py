from application.zone.ZoneMapper import ZoneMapper
from domain.model.environment import EnvironmentName
from domain.model.zone import Zone, ZoneName
from .ZoneDTOImpl import ZoneDTOImpl


class ZoneMapperImpl(ZoneMapper):
    def dto2domain(self, dto: ZoneDTOImpl) -> Zone:
        return Zone(ZoneName(dto.zone_name), EnvironmentName(dto.environment_name))

    def domain2dto(self, dom: Zone) -> ZoneDTOImpl:
        return ZoneDTOImpl(dom.zone_name.value, dom.environment.value)
