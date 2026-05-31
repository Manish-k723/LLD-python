class Location:
    _next_id = 1
    def __init__(self, name, capacity):
        self.id = Location._next_id
        Location._next_id += 1

        self.name = name
        self.capacity = capacity