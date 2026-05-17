class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content


class Printer:
    def __init__(self, name: str, printer_type: str):
        self.name = name
        self.type = printer_type

    def turn_on(self):
        print(f"Turning on {self.name}")

    def shutdown(self):
        print(f"Shutting down {self.name}")

    def print_document(self, document: Document) -> None:
        self.turn_on()
        print(f"Printing {document.title} using {self.name}")
        self.shutdown()

d1 = Document("Report", "This is a report")
d2 = Document("Invoice", "This is an invoice")

printer = Printer("HP LaserJet", "HP LaserJet")
printer.print_document(d1)




