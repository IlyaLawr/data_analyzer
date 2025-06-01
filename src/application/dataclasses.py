from dataclasses import dataclass

@dataclass
class Context:
    _data = []

    def set_message(self, message: str, role: str) -> None:
        self._data.append(message)
        self._data.append(role)

    def get_context(self) -> list[str]:
        return self._data
