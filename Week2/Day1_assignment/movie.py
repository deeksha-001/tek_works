class Cinema:
    def __init__(self, movies):
        self.movies = movies   

    def book(self, movie, seats):
        if movie not in self.movies:
            return f"{movie} not available"
        if self.movies[movie] < seats:
            return "Not enough seats available"
        self.movies[movie] -= seats
        return f"Booked {seats} tickets for {movie}"

    def cancel(self, movie, seats):
        if movie not in self.movies:
            return f"{movie} not available"
        self.movies[movie] += seats
        return f"Cancelled {seats} ticket for {movie}"

    def show_movies(self):
        print(f"Movies: {self.movies}")


cinema = Cinema({"Avatar": 10, "Batman": 5})

print(cinema.book("Avatar", 2))
print(cinema.cancel("Avatar", 1))
cinema.show_movies()
