class Event:
    def __init__(
        self,
        event_title,
        date_of_event,
        time_of_event,
        venue_name,
        total_num_seats,
        seats_available,
        price_per_ticket,
        event_category,
    ):
        self.event_title = event_title
        self.date_of_event = date_of_event
        self.time_of_event = time_of_event
        self.venue_name = venue_name
        self.total_num_seats = total_num_seats
        self.seats_available = seats_available
        self.price_per_ticket = price_per_ticket
        self.event_category = event_category
