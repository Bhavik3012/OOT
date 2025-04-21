# Online Booking System - Object-Oriented Prototype in Python (Full Version)

import csv
from datetime import datetime
from abc import ABC, abstractmethod

# ==============================
# Abstract Class: User
# ==============================
class User(ABC):
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password

# ==============================
# Customer Class
# ==============================
class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.bookings = []

    def make_booking(self, booking):
        self.bookings.append(booking)
        print(f"Booking made successfully for {self.name}.")

# ==============================
# Admin Class
# ==============================
class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def view_users(self, users):
        print("\n--- Registered Users ---")
        for user in users.values():
            print(f"ID: {user.user_id}, Name: {user.name}, Email: {user.email}")

# ==============================
# Abstract Class: Service
# ==============================
class Service(ABC):
    def __init__(self, service_id, service_name, origin, destination, date, price):
        self.service_id = service_id
        self.service_name = service_name
        self.origin = origin
        self.destination = destination
        self.date = date
        self.price = float(price)

    @abstractmethod
    def get_info(self):
        pass

# ==============================
# Travel Services
# ==============================
class FlightService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, seats):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.seats = int(seats)

    def get_info(self):
        return f"[Flight] {self.service_name} | {self.origin} to {self.destination} | Date: {self.date} | ₹{self.price} | Seats: {self.seats}"

class BusService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, seats):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.seats = int(seats)

    def get_info(self):
        return f"[Bus] {self.service_name} | {self.origin} to {self.destination} | Date: {self.date} | ₹{self.price} | Seats: {self.seats}"

class TrainService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, seats):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.seats = int(seats)

    def get_info(self):
        return f"[Train] {self.service_name} | {self.origin} to {self.destination} | Date: {self.date} | ₹{self.price} | Seats: {self.seats}"

class TripService(Service):
    def get_info(self):
        return f"[Trip] {self.service_name} | {self.origin} to {self.destination} | Date: {self.date} | ₹{self.price}"

# ==============================
# Stay Services
# ==============================
class HotelService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, contact, rooms):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.contact = contact
        self.rooms = int(rooms)

    def get_info(self):
        return f"[Hotel] {self.service_name} | {self.origin} | Date: {self.date} | ₹{self.price} | Contact: {self.contact} | Rooms: {self.rooms}"

class HomestayService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, contact):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.contact = contact

    def get_info(self):
        return f"[Homestay] {self.service_name} | {self.origin} | Date: {self.date} | ₹{self.price} | Contact: {self.contact}"

class FarmhouseService(Service):
    def __init__(self, service_id, service_name, origin, destination, date, price, contact):
        super().__init__(service_id, service_name, origin, destination, date, price)
        self.contact = contact

    def get_info(self):
        return f"[Farmhouse] {self.service_name} | {self.origin} | Date: {self.date} | ₹{self.price} | Contact: {self.contact}"

# ==============================
# Booking, Payment, Notification
# ==============================
class Booking:
    def __init__(self, booking_id, customer, service, booking_date):
        self.booking_id = booking_id
        self.customer = customer
        self.service = service
        self.booking_date = booking_date

    def __str__(self):
        return f"BookingID: {self.booking_id}, Customer: {self.customer.name}, Service: {self.service.get_info()}, Date: {self.booking_date}"

class Payment:
    def __init__(self, booking, amount):
        self.booking = booking
        self.amount = amount
        self.date = datetime.now()

    def process(self):
        print(f"Payment of ₹{self.amount} successful for {self.booking.customer.name} on {self.date}.")

class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message

    def send(self):
        print(f"[Notification to {self.user.name}] {self.message}")

# ==============================
# Utility Functions
# ==============================

def update_seat_availability(filename, service_id, new_seat_count):
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            if row['service_id'] == service_id:
                row['seats'] = str(new_seat_count)
            rows.append(row)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

def update_room_availability(filename, service_id, new_room_count):
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            if row['service_id'] == service_id:
                row['rooms'] = str(new_room_count)
            rows.append(row)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

def update_seat_availability(filename, service_id, new_seat_count):
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            if row['service_id'] == service_id:
                row['seats'] = str(new_seat_count)
            rows.append(row)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
def load_users():
    users = {}
    try:
        with open('users.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user_id'].startswith('A'):
                    user = Admin(row['user_id'], row['name'], row['email'], row['password'])
                else:
                    user = Customer(row['user_id'], row['name'], row['email'], row['password'])
                users[user.user_id] = user
    except FileNotFoundError:
        admin = Admin("A001", "System Admin", "admin@booking.com", "admin123")
        users[admin.user_id] = admin
    return users

def save_user(user):
    fieldnames = ['user_id', 'name', 'email', 'password']
    file_exists = False
    try:
        with open('users.csv', 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass
    with open('users.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        })

def load_services(filename, service_type):
    services = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if service_type == 'flight':
                    service = FlightService(**row)
                elif service_type == 'bus':
                    service = BusService(**row)
                elif service_type == 'train':
                    service = TrainService(**row)
                elif service_type == 'trip':
                    service = TripService(**row)
                elif service_type == 'hotel':
                    service = HotelService(**row)
                elif service_type == 'homestay':
                    service = HomestayService(**row)
                elif service_type == 'farmhouse':
                    service = FarmhouseService(**row)
                else:
                    continue
                services.append(service)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return services

# ==============================
# Admin Utilities
# ==============================

def update_seat_availability(filename, service_id, new_seat_count):
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            if row['service_id'] == service_id:
                row['seats'] = str(new_seat_count)
            rows.append(row)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
def view_services_for_admin(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i, row in enumerate(rows):
                print(f"{i}. {row}")
            return rows
    except FileNotFoundError:
        print("File not found.")
        return []

def add_service_to_csv(filename, headers):
    new_row = []
    print("Enter new service details:")
    for header in headers:
        new_row.append(input(f"{header}: "))
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
    print("New service added successfully.")

def remove_service_from_csv(filename):
    rows = view_services_for_admin(filename)
    if not rows:
        return
    try:
        index = int(input("Enter the index of the service to remove: "))
        if 0 < index < len(rows):
            del rows[index]
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Service removed successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

# ==============================
# Main Program (with Trip Support)
# ==============================
if __name__ == "__main__":
    users = load_users()
    print("1. Login\n2. Register\n3. Admin Login")
    choice = input("Choose an option: ")

    if choice == '1':
        uid = input("User ID: ")
        pw = input("Password: ")
        user = users.get(uid)
        if user and user.password == pw:
            print(f"\nWelcome, {user.name}!")
            while True:
                print("\n1. Book Travel\n2. Book Stay\n3. Book Trip\n4. View Bookings\n5. Exit")
                action = input("Choose category: ")
                if action == '1':
                    travel_type = input("Choose Travel Type (flight/train/bus): ").strip().lower()
                    if travel_type not in ['flight', 'train', 'bus']:
                        print("Invalid travel type selected.")
                        continue
                    service_map = {
                        'flight': ("flights.csv", 'flight'),
                        'train': ("trains.csv", 'train'),
                        'bus': ("buses.csv", 'bus')
                    }
                elif action == '2':
                    travel_type = input("Choose Stay Type (hotel/homestay/farmhouse): ").strip().lower()
                    if travel_type not in ['hotel', 'homestay', 'farmhouse']:
                        print("Invalid stay type selected.")
                        continue
                    service_map = {
                        'hotel': ("hotels.csv", 'hotel'),
                        'homestay': ("homestays.csv", 'homestay'),
                        'farmhouse': ("farmhouses.csv", 'farmhouse')
                    }
                elif action == '3':
                    travel_type = 'trip'
                    service_map = {
                        'trip': ("trips.csv", 'trip')
                    }
                elif action == '4':
                    if isinstance(user, Customer):
                        if user.bookings:
                            print("\n--- Your Bookings ---")
                            for booking in user.bookings:
                                print(booking)
                        else:
                            print("You have no bookings yet.")
                    continue
                elif action == '5':
                    print("Thank you for using the booking system!")
                    break
                else:
                    print("Invalid category.")
                    continue

                filename, service_type = service_map.get(travel_type, (None, None))
                if filename:
                    services = load_services(filename, service_type)
                    if not services:
                        print("No services available.")
                        continue
                    print("\nAvailable Options:")
                    for i, s in enumerate(services):
                        print(f"{i+1}. {s.get_info()}")
                    try:
                        choice = int(input("Select a service by number: ")) - 1
                        if 0 <= choice < len(services):
                            selected = services[choice]
                            if hasattr(selected, 'seats'):
                                try:
                                    seats_required = int(input("Enter number of seats to book: "))
                                    if seats_required <= selected.seats:
                                        selected.seats -= seats_required
                                        total_price = selected.price * seats_required
                                    else:
                                        print("Not enough seats available.")
                                        continue
                                except ValueError:
                                    print("Invalid number of seats.")
                                    continue
                            else:
                                seats_required = 1
                                total_price = selected.price
                            booking_id = f"B{datetime.now().strftime('%Y%m%d%H%M%S')}"
                            booking = Booking(booking_id, user, selected, datetime.now())
                            user.make_booking(booking)
                            payment = Payment(booking, total_price)
                            payment.process()
                            Notification(user, "Your booking is confirmed!").send()
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Invalid service type selected.")
        else:
            print("Invalid credentials.")

    elif choice == '2':
        uid = input("Enter new user ID: ")
        if uid in users:
            print("User ID already exists. Please choose another.")
        else:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            pw = input("Enter your password: ")
            user = Customer(uid, name, email, pw)
            save_user(user)
            users[uid] = user
            print("Registration successful. You can now login.")

    elif choice == '3':
        admin_email = input("Enter admin email: ")
        admin_pw = input("Enter admin password: ")
        if admin_email == "admin@booking.com" and admin_pw == "admin123":
            admin = Admin("A001", "System Admin", admin_email, admin_pw)
            print("\nWelcome Admin!")
            while True:
                print("--- Admin Menu ---")
                print("1. View Users\n2. Add Service Availability\n3. Remove Service Availability\n4. Logout")
                option = input("Choose an action: ")
                if option == '1':
                    admin.view_users(users)
                elif option == '2':
                    print("Choose service type (flight/bus/train/trip/hotel/homestay/farmhouse):")
                    s_type = input().strip().lower()
                    filenames = {
                        'flight': ("flights.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'bus': ("buses.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'train': ("trains.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'trip': ("trips.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'hotel': ("hotels.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'homestay': ("homestays.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                        'farmhouse': ("farmhouses.csv", ["service_id", "service_name", "origin", "destination", "date", "price"]),
                    }
                    file_info = filenames.get(s_type)
                    if file_info:
                        add_service_to_csv(*file_info)
                    else:
                        print("Invalid type.")
                elif option == '3':
                    print("Choose service type (flight/bus/train/trip/hotel/homestay/farmhouse):")
                    s_type = input().strip().lower()
                    file_map = {
                        'flight': "flights.csv",
                        'bus': "buses.csv",
                        'train': "trains.csv",
                        'trip': "trips.csv",
                        'hotel': "hotels.csv",
                        'homestay': "homestays.csv",
                        'farmhouse': "farmhouses.csv",
                    }
                    filename = file_map.get(s_type)
                    if filename:
                        remove_service_from_csv(filename)
                    else:
                        print("Invalid type.")
                elif option == '4':
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid admin credentials.")

    else:
        print("Invalid option selected.")
