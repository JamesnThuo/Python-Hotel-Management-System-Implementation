from datetime import datetime, timedelta

class Booking:
    """Class representing a room booking"""
    
    def __init__(self, guest, room, check_in_date, check_out_date):
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_date = datetime.now().date()
        self._status = "Confirmed"
        self._invoice = None
        self._additional_services = []
    
    # Getters
    @property
    def guest(self):
        return self._guest
    
    @property
    def room(self):
        return self._room
    
    @property
    def check_in_date(self):
        return self._check_in_date
    
    @property
    def check_out_date(self):
        return self._check_out_date
    
    @property
    def booking_date(self):
        return self._booking_date
    
    @property
    def status(self):
        return self._status
    
    @property
    def invoice(self):
        return self._invoice
    
    @property
    def additional_services(self):
        return self._additional_services
    
    # Setters
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    def calculate_stay_duration(self):
        """Calculate the number of nights for the stay"""
        return (self._check_out_date - self._check_in_date).days
    
    def generate_invoice(self):
        """Generate an invoice for the booking"""
        if not self._invoice:
            self._invoice = Invoice(self)
        return self._invoice
    
    def add_service(self, service):
        """Add an additional service to the booking"""
        self._additional_services.append(service)
        if self._invoice:
            self._invoice._update_invoice()
    
    def cancel_booking(self):
        """Cancel the booking"""
        self._status = "Cancelled"
        self._room.is_available = True
        return True
    
    def __str__(self):
        return (f"Booking for {self._guest.name}\n"
                f"Room: {self._room.room_number} ({self._room.room_type})\n"
                f"Check-in: {self._check_in_date}\n"
                f"Check-out: {self._check_out_date}\n"
                f"Status: {self._status}\n"
                f"Duration: {self.calculate_stay_duration()} nights")


class Invoice:
    """Class representing an invoice for a booking"""
    
    def __init__(self, booking):
        """Initialize an invoice"""
        self._booking = booking
        self._invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._issue_date = datetime.now().date()
        self._items = []
        self._total_amount = 0
        self._update_invoice()
    
    @property
    def booking(self):
        return self._booking
    
    @property
    def invoice_number(self):
        return self._invoice_number
    
    @property
    def issue_date(self):
        return self._issue_date
    
    @property
    def items(self):
        return self._items
    
    @property
    def total_amount(self):
        return self._total_amount
    
    def _update_invoice(self):
        """Update the invoice items and total amount"""
        self._items = []
        
        # Room charges
        nights = self._booking.calculate_stay_duration()
        room_total = nights * self._booking.room.price_per_night
        self._items.append({
            'description': f"Room {self._booking.room.room_number} ({nights} nights)",
            'amount': room_total
        })
        
        # Additional services
        for service in self._booking.additional_services:
            self._items.append({
                'description': service.description,
                'amount': service.price
            })
        
        # Calculate total
        self._total_amount = sum(item['amount'] for item in self._items)
        
        # Apply loyalty discount if applicable
        if self._booking.guest.loyalty_program:
            discount = min(self._booking.guest.loyalty_program.points * 0.1, self._total_amount * 0.2)
            if discount > 0:
                self._items.append({
                    'description': "Loyalty Discount",
                    'amount': -discount
                })
                self._total_amount -= discount
    
    def __str__(self):
        invoice_str = (f"Invoice {self._invoice_number}\n"
                      f"Issue Date: {self._issue_date}\n"
                      f"Guest: {self._booking.guest.name}\n"
                      f"Room: {self._booking.room.room_number}\n"
                      f"Check-in: {self._booking.check_in_date}\n"
                      f"Check-out: {self._booking.check_out_date}\n\n"
                      f"Items:\n")
        
        for item in self._items:
            invoice_str += f"{item['description']:50} ${item['amount']:8.2f}\n"
        
        invoice_str += f"\n{'Total Amount':50} ${self._total_amount:8.2f}"
        
        return invoice_str