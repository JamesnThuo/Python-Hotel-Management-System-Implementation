from datetime import datetime, timedelta
from room import StandardRoom, DeluxeRoom, Suite
from guest import Guest
from booking import Booking
from payment import CreditCardPayment, DebitCardPayment, MobileWalletPayment
from service import Housekeeping, RoomService, Transportation
from feedback import Feedback

class HotelSystem:
    def __init__(self):
        self._rooms = []
        self._guests = []
        self._bookings = []
        self._feedbacks = []
        self._initialize_sample_data()
    
    def get_rooms(self):
        return self._rooms
    
    def get_guests(self):
        return self._guests
    
    def get_bookings(self):
        return self._bookings
    
    def get_feedbacks(self):
        return self._feedbacks
    
    def _initialize_sample_data(self):
        self._rooms.extend([
            StandardRoom("101", 99.99),
            StandardRoom("102", 99.99),
            DeluxeRoom("201", 149.99),
            DeluxeRoom("202", 149.99),
            Suite("301", 249.99),
            Suite("302", 249.99)
        ])
        
        self._guests.extend([
            Guest("John Doe", "john@example.com", "555-0101"),
            Guest("Jane Smith", "jane@example.com", "555-0102"),
            Guest("Robert Johnson", "robert@example.com", "555-0103")
        ])
        
        self._guests[0].enroll_in_loyalty_program().add_points(300)
        self._guests[1].enroll_in_loyalty_program().add_points(750)
    
    def register_guest(self, name, email, phone, address=None):
        new_guest = Guest(name, email, phone, address)
        self._guests.append(new_guest)
        return new_guest
    
    def find_available_rooms(self, room_type=None, check_in=None, check_out=None):
        available_rooms = [room for room in self._rooms if room.is_available()]
        
        if room_type:
            available_rooms = [room for room in available_rooms if room.get_room_type().lower() == room_type.lower()]
        
        return available_rooms
    
    def create_booking(self, guest, room, check_in, check_out):
        if not room.is_available():
            raise ValueError("Room is not available")
        
        booking = Booking(guest, room, check_in, check_out)
        self._bookings.append(booking)
        guest.add_booking(booking)
        room.set_available(False)
        return booking
    
    def process_payment(self, booking, payment_method, payment_details):
        invoice = booking.generate_invoice()
        today = datetime.now().date()
        
        if payment_method.lower() == 'credit':
            payment = CreditCardPayment(
                invoice.get_total_amount(), today,
                payment_details['card_number'],
                payment_details['card_holder'],
                payment_details['expiry_date'],
                payment_details['cvv']
            )
        elif payment_method.lower() == 'debit':
            payment = DebitCardPayment(
                invoice.get_total_amount(), today,
                payment_details['card_number'],
                payment_details['card_holder'],
                payment_details['expiry_date'],
                payment_details['cvv']
            )
        elif payment_method.lower() == 'mobile':
            payment = MobileWalletPayment(
                invoice.get_total_amount(), today,
                payment_details['wallet_type'],
                payment_details['phone_number']
            )
        else:
            raise ValueError("Invalid payment method")
        
        payment.process_payment()
        return payment
    
    def add_service_request(self, booking, service_type, service_details):
        today = datetime.now()
        
        if service_type.lower() == 'housekeeping':
            service = Housekeeping(today, booking.get_room(), service_details.get('service_type', 'Standard'))
        elif service_type.lower() == 'roomservice':
            service = RoomService(today, booking.get_room(), service_details['items'])
        elif service_type.lower() == 'transportation':
            service = Transportation(
                today, booking.get_room(),
                service_details['vehicle_type'],
                service_details['destination']
            )
        else:
            raise ValueError("Invalid service type")
        
        booking.add_service(service)
        return service
    
    def submit_feedback(self, guest, rating, comments, stay_date=None):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        feedback = Feedback(guest, rating, comments, stay_date)
        self._feedbacks.append(feedback)
        return feedback
    
    def __str__(self):
        return (f"Royal Stay Hotel Management System\n"
                f"Rooms: {len(self._rooms)}\n"
                f"Guests: {len(self._guests)}\n"
                f"Bookings: {len(self._bookings)}\n"
                f"Feedbacks: {len(self._feedbacks)}")