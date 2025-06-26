"""UDS addresses of ECUs for communication over OBD-2 CAN bus (pins 6 and 14 of OBD-2 port)."""

__all__ = [
    'ECU_39106_08254',
    'ECU_56340_Q0100',
    'ECU_58910_Q0200',
    'ECU_91953_Q0530',
    "ECU_94023_Q0221",
    'ECU_95400_Q0030',
    'ECU_95910_Q0100',
    'ECU_96160_Q0420',
    'ECU_96510_Q0000',
    'ECU_99211_Q0100',
    'ECU_99240_Q0000'
]


from uds.can import CanAddressingFormat, CanAddressingInformation

ECU_39106_08254 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7E0},
                                           rx_physical={"can_id": 0x7E8},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7E8})
"""
Engine Control Unit for Hyundai i20.
SPARE PART NUMBER: 39106-08254

.. seealso:: https://www.hyundai-pieces.com/oem-39106-08254.html
"""

ECU_56340_Q0100 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7D4},
                                           rx_physical={"can_id": 0x7DC},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7DC})
"""
Steering Column for Hyundai i20.
SPARE PART NUMBER: 56340-Q0100
"""

ECU_58910_Q0200 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7D1},
                                           rx_physical={"can_id": 0x7D9},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7D9})
"""
ABS Pump for Hyundai i20.
SPARE PART NUMBER: 58910-Q0200
"""

ECU_91953_Q0530 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x770},
                                           rx_physical={"can_id": 0x778},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x778})
"""
Body Control Module for Hyundai i20 Comfort/Convience.
SPARE PART NUMBER: 91953-Q0530
"""

ECU_94023_Q0221 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7C6},
                                           rx_physical={"can_id": 0x7CE},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7CE})
"""
SPEEDOMETER/INSTRUMENT CLUSTER for Hyundai i20 and Bayon (Petrol).
SPARE PART NUMBER: 94023-Q0221
"""

ECU_95400_Q0030 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7A0},
                                           rx_physical={"can_id": 0x7A8},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7A8})
"""
Break Control Module Unite for Hyundai i20.
SPARE PART NUMBER: 95400-Q0030

.. seealso:: https://www.hyundaipartsdeal.com/genuine/hyundai-unit-assy-bcm~95400-3q000.html
"""

ECU_95910_Q0100 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7D2},
                                           rx_physical={"can_id": 0x7DA},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7DA})
"""
Airbag ECU for Hyundai i20.
SPARE PART NUMBER: 95910-Q0100

.. seealso:: https://www.hyundai-pieces.com/oem-95910-Q0100.html
"""

ECU_96160_Q0420 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x780},
                                           rx_physical={"can_id": 0x788},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x788})
"""
Sat Nav Screen display for Hyundai i20/Bayon.
SPARE PART NUMBER: 96160-Q0420
"""

ECU_96510_Q0000 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7C7},
                                           rx_physical={"can_id": 0x7CF},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7CF})
"""
Wireless roof antenna control module for Hyundai i20/Bayon.
SPARE PART NUMBER: 96510-Q0000
"""


ECU_99211_Q0100 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x7C4},
                                           rx_physical={"can_id": 0x7CC},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x7CC})
"""
Front Windscreen Lane Assist Camera for Hyundai i20/Bayon.
SPARE PART NUMBER: 99211-Q0100

.. seealso:: https://www.hyundai-pieces.com/oem-99211-Q0100.html
"""

ECU_99240_Q0000 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                           tx_physical={"can_id": 0x796},
                                           rx_physical={"can_id": 0x79E},
                                           tx_functional={"can_id": 0x7DF},
                                           rx_functional={"can_id": 0x79E})
"""
Rear View Camera for Hyundai i20.
SPARE PART NUMBER: 99240-Q0000
"""