class Booking:
    def __init__(
        self,
        booking_reference,
        event_id,
        customer_id,
        ticket_quantity,
        total_price,
        date_of_booking,
    ):
        self.booking_reference = booking_reference
        self.event_id = event_id
        self.customer_id = customer_id
        self.ticket_quantity = ticket_quantity
        self.total_price = total_price
        self.date_of_booking = date_of_booking
