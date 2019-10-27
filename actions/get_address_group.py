from lib.action import FortinetBaseAction


class GetAddressGroup(FortinetBaseAction):
    def run(self, name=None, output_format=''):
        addresses = self.device.get_address_group(name)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
