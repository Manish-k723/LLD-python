class Board:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if getattr(self, "_initialized", False):
            return 
        self._initialized = True
        self.resetBoard()
        
    def resetBoard(self):
        pass
    
    
    def display(self):
        pass