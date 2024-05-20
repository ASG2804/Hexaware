from Entity import Booking, Customers, Events, Venues
from DAO import EventService, BookingSystem


def main():
    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Seats")
        print("5. Get Event Details")
        print("6. Calculate Booking Cost")
        print("7. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            event_title = input("Enter event name: ")
            date_of_event = input("Enter event date (YYYY-MM-DD): ")
            time_of_event = input("Enter event time (HH:MM:SS): ")
            total_num_seats = int(input("Enter total number of seats: "))
            seats_available = int(input("Enter the available seats:"))
            price_per_ticket = float(input("Enter ticket price: "))
            event_category = input("Enter event type (Movie/Sports/Concert): ")
            Venues.venue_id = input("Enter venue id:")
            new_event = Events(
                event_title,
                date_of_event,
                time_of_event,
                total_num_seats,
                seats_available,
                price_per_ticket,
                event_category,
                Venues.Venue.venue_id,
            )
            EventService.create_event(new_event)
        elif user_choice == "2":
            try:
                event_title = input("Enter event name to book tickets: ")
                ticket_quantity = int(input("Enter the number of tickets to book: "))
                date_of_booking = input("Enter booking date (YYYY-MM-DD): ")
                customer_list = []
                # You need to define and populate this list with customer IDs
                BookingSystem.book_tickets(
                    event_title, ticket_quantity, date_of_booking, customer_list
                )
            except Exception as e:
                print("Error booking tickets:", e)
        elif user_choice == "3":
            try:
                booking_reference = input("Enter booking ID to cancel: ")
                BookingSystem.cancel_booking(booking_reference)
            except Exception as e:
                print("Error canceling booking:", e)
        elif user_choice == "4":
            try:
                seats_available = EventService.getAvailableNoOfTickets()
                if seats_available:
                    print("\nTotal Available Seats:", seats_available)
                else:
                    print("No available seats found.")
            except Exception as e:
                print("Error fetching available seats:", e)
        elif user_choice == "5":
            try:
                EventService.getEventDetails()
            except Exception as e:
                print("Error fetching event details:", e)
        elif user_choice == "6":
            print("Exiting...")
            break
        elif user_choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
