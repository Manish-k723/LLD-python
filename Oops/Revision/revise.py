class Movie:
    def __init__(self, name, seats, price) -> None:
        self.name = name
        self.seats = seats
        self.price = price
        self.booked = 0


    def book(self, num_of_tickets: int) -> str:
        if self.seats - self.booked < num_of_tickets:
            return "Sorry, the movie is full"
        self.booked += num_of_tickets
        return self.price * num_of_tickets

    def status(self) -> None:
        print(f"The movie {self.name} is {self.booked}/{self.seats} seats booked")
m1 = Movie("Avengers", 3, 10000)
m1.status()
print(m1.book(3))
m1.status()

