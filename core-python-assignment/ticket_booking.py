def available_seats(total, booked):
    return [s for s in range(1, total + 1) if s not in booked]

def book_seat(booked, seat):
    if seat not in booked:
        booked.append(seat)
        print("Seat", seat, "booked.")
    else:
        print("Seat", seat, "is already booked.")

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
        print("Seat", seat, "canceled.")
    else:
        print("Seat", seat, "was not booked.")

total_seats = 10
booked_seats = [2, 5, 7]

book_seat(booked_seats, 3)
cancel_seat(booked_seats, 5)

print("Available seats:", available_seats(total_seats, booked_seats))
