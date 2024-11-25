class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.room_number} ({self.room_type}) is successfully booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def vacate_room(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Room {self.room_number} is now available.")
        else:
            print(f"Room {self.room_number} is already vacant.")


class CafeMenu:
    def __init__(self):
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 100,
            "Burger": 150,
            "Pasta": 200
        }

    def display_menu(self):
        print("\n📋 Café Menu:")
        for item, price in self.menu.items():
            print(f"   {item}: ₹{price}")

    def get_price(self, item):
        return self.menu.get(item, None)


class HotelAndCafeManagementSystem:
    def __init__(self):
        self.rooms = [
            Room(101, "Single", 1000),
            Room(102, "Double", 1500),
            Room(103, "Suite", 3000),
        ]
        self.cafe = CafeMenu()

    def display_rooms(self):
        print("\n🏨 Room Details:")
        for room in self.rooms:
            status = "Booked" if room.is_booked else "Available"
            print(f"   Room {room.room_number} ({room.room_type}): ₹{room.price_per_night}/night [{status}]")

    def book_room(self):
        self.display_rooms()
        room_number = int(input("\nEnter the room number to book: "))
        for room in self.rooms:
            if room.room_number == room_number:
                room.book_room()
                return
        print("Invalid room number.")

    def vacate_room(self):
        room_number = int(input("\nEnter the room number to vacate: "))
        for room in self.rooms:
            if room.room_number == room_number:
                room.vacate_room()
                return
        print("Invalid room number.")

    def order_food(self):
        self.cafe.display_menu()
        total_bill = 0
        while True:
            order = input("\nEnter the item to order (or type 'done' to finish): ").title()
            if order == 'Done':
                break
            price = self.cafe.get_price(order)
            if price:
                total_bill += price
                print(f"Added {order} to your order. Price: ₹{price}")
            else:
                print("Invalid item. Please select from the menu.")
        print(f"\n🧾 Total Bill for your order: ₹{total_bill}")

    def main_menu(self):
        while True:
            print("\n📋 Hotel and Café Management System")
            print("1. Display Room Details")
            print("2. Book a Room")
            print("3. Vacate a Room")
            print("4. Order Food")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_rooms()
            elif choice == "2":
                self.book_room()
            elif choice == "3":
                self.vacate_room()
            elif choice == "4":
                self.order_food()
            elif choice == "5":
                print("Thank you for using the Hotel and Café Management System! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = HotelAndCafeManagementSystem()
    system.main_menu()
