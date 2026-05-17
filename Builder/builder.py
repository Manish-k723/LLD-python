class Laptop:
    processor = None
    cpu = None
    colors = None
    ram = None
    display = None

    def __str__(self):
        return f"Processor: {self.processor}\nCPU: {self.cpu}\nColors: {self.colors}\nRAM: {self.ram}\nDisplay: {self.display}"

class LaptopBuilder:
    def __init__(self):
        self._laptop = Laptop()

    def build_processor(self, processor):
        self._laptop.processor = processor
        return self

    def build_cpu(self, cpu):
        self._laptop.cpu = cpu
        return self

    def build_colors(self, colors):
        self._laptop.colors = colors
        return self

    def build_ram(self, ram):
        self._laptop.ram = ram
        return self

    def build_display(self, display):
        self._laptop.display = display
        return self

    def build(self):
        return self._laptop

laptop = LaptopBuilder().build_cpu("12th Gen").build_colors("Black").build_ram("16GB").build_display("15.6 inch").build()
print(laptop)