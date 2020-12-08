class ZoneConnectionModel(object):

    def __init__(self, source_id: int, destination_id: int, firewall_id: int, criticality: int,
                 uuid,
                 allowed_ports=None):
        if allowed_ports is None:
            allowed_ports = []
        self.source_id = source_id
        self.destination_id = destination_id
        self.firewall_id = firewall_id
        self.criticality = criticality
        self.uuid = uuid
        self.allowed_ports = allowed_ports
