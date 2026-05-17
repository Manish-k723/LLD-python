class Logger:
    __instance = None
    __initialized = False
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, file_name: str = "default.log"):
        if not self.__initialized:
            self.__file_name = file_name
            self.__log_count = 0

    def get_file_name(self) -> str:
        return self.__file_name


log1 = Logger()
print(log1)
print(log1.get_file_name())

log2 = Logger()
print(log2)