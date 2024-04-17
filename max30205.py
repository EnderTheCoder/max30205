import smbus


class MAX30205:
    def __init__(self, address):
        self._address = address
        self._bus = smbus.SMBus(1)

    def read_temperature(self):
        temperature_data = self._bus.read_i2c_block_data(self._address, 0x00, 2)
        raw_temperature = (temperature_data[0] << 8) | temperature_data[1]
        return raw_temperature * 0.00390625
