class Gate:
    def __init__(self, gate_number: int):
        self._gate_number = gate_number

    def get_gate_number(self) -> int:
        return self._gate_number
