"""ECUs Addresses on CAN bus that is accessible via OBD-2 port (pins 6 and 14)."""

__all__ = [
    "ABS_PUMP",
    "AIRBAG_ECU",
    "BODY_CONTROL_MODULE",
    "BREAK_CONTROL_MODULE",
    "ENGINE_CONTROL_UNIT",
    "FRONT_CAMERA",
    "NAVIGATION_SCREEN",
    "REAR_CAMERA",
    "STEERING_COLUMN",
    "WIRELESS_ROOF_ANTENNA",
    "UNKNOWN_ECU_1",
    "UNKNOWN_ECU_2",
    "UNKNOWN_ECU_3"
]

from uds.can import CanAddressingFormat, CanAddressingInformation

from uds_address.ecu.can import (
    ECU_39106_08254,
    ECU_56340_Q0100,
    ECU_58910_Q0200,
    ECU_91953_Q0530,
    ECU_95400_Q0030,
    ECU_95910_Q0100,
    ECU_96160_Q0420,
    ECU_96510_Q0000,
    ECU_99211_Q0100,
    ECU_99240_Q0000,
)

ABS_PUMP = ECU_58910_Q0200
AIRBAG_ECU = ECU_95910_Q0100
BODY_CONTROL_MODULE = ECU_91953_Q0530
BREAK_CONTROL_MODULE = ECU_95400_Q0030
ENGINE_CONTROL_UNIT = ECU_39106_08254
FRONT_CAMERA = ECU_99211_Q0100
NAVIGATION_SCREEN = ECU_96160_Q0420
REAR_CAMERA = ECU_99240_Q0000
STEERING_COLUMN = ECU_56340_Q0100
WIRELESS_ROOF_ANTENNA = ECU_96510_Q0000

UNKNOWN_ECU_1 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                         tx_physical={"can_id": 0x7B3},
                                         rx_physical={"can_id": 0x7BB},
                                         tx_functional={"can_id": 0x7DF},
                                         rx_functional={"can_id": 0x7BB})

UNKNOWN_ECU_2 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                         tx_physical={"can_id": 0x7C6},
                                         rx_physical={"can_id": 0x7CE},
                                         tx_functional={"can_id": 0x7DF},
                                         rx_functional={"can_id": 0x7CE})
# SPARE PART NUMBER = 940?? (missing the rest due to ECU communication issue)

UNKNOWN_ECU_3 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                         tx_physical={"can_id": 0x7F1},
                                         rx_physical={"can_id": 0x7F9},
                                         tx_functional={"can_id": 0x7DF},
                                         rx_functional={"can_id": 0x7F9})
