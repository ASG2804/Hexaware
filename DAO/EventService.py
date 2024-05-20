from Entity import Venues, Events
from Util.DBconnenction import DBConnection


class event_Service_Provider(DBConnection):
    def create_event(self, new_event):
        try:
            self.cursor.execute(
                """
                INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type, venue_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    new_event.event_name,
                    new_event.event_date,
                    new_event.event_time,
                    new_event.total_seats,
                    new_event.available_seats,
                    new_event.ticket_price,
                    new_event.event_type,
                    Venues.venue_id,
                ),
            )
            self.conn.commit()
            print("Event created successfully")
        except Exception as e:
            print(e)

    def getEventDetails(self):
        try:
            print("Select the type of event details you want to see:")
            print("1. Movie event details")
            print("2. Concert event details")
            print("3. Sports event details")
            event_choice = int(input("Enter your choice (1/2/3): "))

            if event_choice == 1:
                event_category = "Movie"
            elif event_choice == 2:
                event_category = "Concert"
            elif event_choice == 3:
                event_category = "Sports"
            else:
                print("Invalid choice. Please enter a valid option.")

            self.cursor.execute(
                "SELECT * FROM Event WHERE event_type = ?", (event_category,)
            )
            event_info = self.cursor.fetchall()
            for event in event_info:
                print(event)

        except Exception as e:
            print(e)

    def getAvailableNoOfTickets(self):
        try:
            self.cursor.execute("SELECT SUM(available_seats) FROM Event")
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)
