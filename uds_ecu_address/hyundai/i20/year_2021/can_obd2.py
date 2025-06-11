"""ECUs Addresses on CAN bus that is accessible via OBD-2 port (pins 6 and 14)."""

__all__ = []

from uds.can import CanAddressingFormat, CanAddressingInformation

# TODO: check each ECU name/responsibility
ECU1 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x770},
                                rx_physical={"can_id": 0x778},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU2 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x780},
                                rx_physical={"can_id": 0x788},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU3 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x796},
                                rx_physical={"can_id": 0x79E},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU4 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7A0},
                                rx_physical={"can_id": 0x7A8},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU5 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7B3},
                                rx_physical={"can_id": 0x7BB},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU6 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7C6},
                                rx_physical={"can_id": 0x7CE},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU7 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7C7},
                                rx_physical={"can_id": 0x7CF},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU8 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7D4},
                                rx_physical={"can_id": 0x7DC},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU9 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                tx_physical={"can_id": 0x7E0},
                                rx_physical={"can_id": 0x7E8},
                                tx_functional={"can_id": 0x7DF},
                                rx_functional={})  # TODO: check

ECU10 = CanAddressingInformation(addressing_format=CanAddressingFormat.NORMAL_11BIT_ADDRESSING,
                                 tx_physical={"can_id": 0x7F1},
                                 rx_physical={"can_id": 0x7F9},
                                 tx_functional={"can_id": 0x7DF},
                                 rx_functional={})  # TODO: check
