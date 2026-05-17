from abc import ABC, abstractmethod

class Parser(ABC):
    def open(self) -> None:
        print("Opening file")

    def close(self) -> None:
        print("Closing file")

    @abstractmethod
    def parse(self) -> None:
        ...

    def template(self) -> None:
        self.open()
        self.parse()
        self.close()