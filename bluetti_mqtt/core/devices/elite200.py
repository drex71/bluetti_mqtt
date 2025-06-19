from enum import Enum, unique
from typing import List
from ..commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from .struct import DeviceStruct


@unique
class OutputMode(Enum):
    STOP = 0
    INVERTER_OUTPUT = 1
    BYPASS_OUTPUT_C = 2
    BYPASS_OUTPUT_D = 3
    LOAD_MATCHING = 4


@unique
class AutoSleepMode(Enum):
    THIRTY_SECONDS = 2
    ONE_MINUTE = 3
    FIVE_MINUTES = 4
    NEVER = 5


class Elite200(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        # Verified: block 160–169
        self.struct.add_uint_field("dc_input_power", 160)
        self.struct.add_uint_field("ac_input_power", 161)
        self.struct.add_uint_field("ac_output_power", 162)
        self.struct.add_uint_field("dc_output_power", 163)
        self.struct.add_uint_field("total_battery_percent", 164)
        self.struct.add_bool_field("ac_output_on", 165)
        self.struct.add_bool_field("dc_output_on", 166)
        self.struct.add_decimal_field("ac_input_voltage", 167, 1)
        self.struct.add_decimal_field("dc_input_voltage1", 168, 1)
        self.struct.add_bool_field("power_off", 169)

        super().__init__(address, "Elite 200", sn)

    @property
    def pack_num_max(self):
        return 1

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return [ReadHoldingRegisters(160, 10)]

    @property
    def pack_polling_commands(self) -> List[ReadHoldingRegisters]:
        return []

    @property
    def logging_commands(self) -> List[ReadHoldingRegisters]:
        return [ReadHoldingRegisters(160, 10)]

    @property
    def pack_logging_commands(self) -> List[ReadHoldingRegisters]:
        return []

    @property
    def writable_ranges(self) -> List[range]:
        return []
