from Util.DBconnenction import DBConnection
from Entity import Booking


class BookingSystemProvider(DBConnection):
    def calculate_booking_cost(self, ticket_quantity):
        try:
            while True:
                print("Select the type of ticket:")
                print("1. Diamond")
                print("2. Gold")
                print("3. Silver")
                ticket_type_choice = int(input("Enter your choice (1/2/3): "))

                if ticket_type_choice == 1:
                    price_per_ticket = 200
                    break
                elif ticket_type_choice == 2:
                    price_per_ticket = 150
                    break
                elif ticket_type_choice == 3:
                    price_per_ticket = 100
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

            total_price = ticket_quantity * price_per_ticket
            return total_price
        except Exception as e:
            print(e)

    def book_tickets(
        self, event_title, ticket_quantity, date_of_booking, customer_list
    ):
        try:
            self.cursor.execute(
                "SELECT event_id FROM Event WHERE event_name = ?", (event_title,)
            )
            event_id = self.cursor.fetchone()[0]
            for customer_id in customer_list:
                total_price = self.calculate_booking_cost(ticket_quantity)
                self.cursor.execute(
                    """
                    INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost, booking_date)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        customer_id,
                        event_id,
                        ticket_quantity,
                        total_price,
                        date_of_booking,
                    ),
                )
                self.conn.commit()

            print("Tickets booked successfully!")
        except Exception as e:
            print(e)

    def cancel_booking(self, booking_reference):
        try:
            self.cursor.execute(
                "SELECT * FROM Booking WHERE booking_id = ?", (booking_reference,)
            )
            booking_info = self.cursor.fetchone()

            if not booking_info:
                print("Booking not found!")
                return
            self.cursor.execute(
                """
                UPDATE Event
                SET available_seats = available_seats + ?
                WHERE event_id = ?
                """,
                (booking_info[3], booking_info[2]),
            )
            self.cursor.execute(
                "DELETE FROM Booking WHERE booking_id = ?", (booking_reference,)
            )
            self.conn.commit()

            print("Booking canceled successfully!")
        except Exception as e:
            print(e)

    def get_booking_details(self, booking_reference):
        try:
            self.cursor.execute(
                "SELECT * FROM Booking WHERE booking_id = ?", (booking_reference,)
            )
            booking_info = self.cursor.fetchone()
            if booking_info:
                booking = Booking(*booking_info)
                return booking
            else:
                print("Booking not found!")
        except Exception as e:
            print(e)
