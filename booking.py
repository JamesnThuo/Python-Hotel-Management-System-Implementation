from datetime import datetime, timedelta

class Booking:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_date = datetime.now().date()
        self._status = "Confirmed"
        self._invoice = None
        self._additional_services = []
    
    def get_guest(self):
        return self._guest
    
    def get_room(self):
        return self._room
    
    def get_check_in_date(self):
        return self._check_in_date
    
    def get_check_out_date(self):
        return self._check_out_date
    
    def get_booking_date(self):
        return self._booking_date
    
    def get_status(self):
        return self._status
    
    def get_invoice(self):
        return self._invoice
    
    def get_additional_services(self):
        return self._additional_services
    
    def set_guest(self, guest):
        self._guest = guest
    
    def set_room(self, room):
        self._room = room
    
    def set_check_in_date(self, check_in_date):
        self._check_in_date = check_in_date
    
    def set_check_out_date(self, check_out_date):
        self._check_out_date = check_out_date
    
    def set_status(self, status):
        self._status = status
    
    def calculate_stay_duration(self):
        return (self._check_out_date - self._check_in_date).days
    
    def generate_invoice(self):
        if not self._invoice:
            self._invoice = Invoice(self)
        return self._invoice
    
    def add_service(self, service):
        self._additional_services.append(service)
        if self._invoice:
            self._invoice.update_invoice()
    
    def cancel_booking(self):
        self._status = "Cancelled"
        self._room.set_available(True)
        return True
    
    def __str__(self):
        return (f"Booking for {self._guest.get_name()}\n"
                f"Room: {self._room.get_room_number()} ({self._room.get_room_type()})\n"
                f"Check-in: {self._check_in_date}\n"
                f"Check-out: {self._check_out_date}\n"
                f"Status: {self._status}\n"
                f"Duration: {self.calculate_stay_duration()} nights")

class Invoice:
    def __init__(self, booking):
        self._booking = booking
        self._invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._issue_date = datetime.now().date()
        self._items = []
        self._total_amount = 0
        self._update_invoice()
    
    def get_booking(self):
        return self._booking
    
    def get_invoice_number(self):
        return self._invoice_number
    
    def get_issue_date(self):
        return self._issue_date
    
    def get_items(self):
        return self._items
    
    def get_total_amount(self):
        return self._total_amount
    
    def _update_invoice(self):
        self._items = []
        nights = self._booking.calculate_stay_duration()
        room_total = nights * self._booking.get_room().get_price_per_night()
        self._items.append({
            'description': f"Room {self._booking.get_room().get_room_number()} ({nights} nights)",
            'amount': room_total
        })
        
        for service in self._booking.get_additional_services():
            self._items.append({
                'description': service.get_description(),
                'amount': service.get_price()
            })
        
        self._total_amount = sum(item['amount'] for item in self._items)
        
        if self._booking.get_guest().get_loyalty_program():
            discount = min(self._booking.get_guest().get_loyalty_program().get_points() * 0.1, 
                          self._total_amount * 0.2)
            if discount > 0:
                self._items.append({
                    'description': "Loyalty Discount",
                    'amount': -discount
                })
                self._total_amount -= discount
    
    def update_invoice(self):
        self._update_invoice()
    
    def __str__(self):
        invoice_str = (f"Invoice {self._invoice_number}\n"
                      f"Issue Date: {self._issue_date}\n"
                      f"Guest: {self._booking.get_guest().get_name()}\n"
                      f"Room: {self._booking.get_room().get_room_number()}\n"
                      f"Check-in: {self._booking.get_check_in_date()}\n"
                      f"Check-out: {self._booking.get_check_out_date()}\n\n"
                      f"Items:\n")
        
        for item in self._items:
            invoice_str += f"{item['description']:50} ${item['amount']:8.2f}\n"
        
        invoice_str += f"\n{'Total Amount':50} ${self._total_amount:8.2f}"
        return invoice_str