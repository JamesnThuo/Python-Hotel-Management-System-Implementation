from datetime import datetime

class Guest:
    """Class representing a hotel guest"""
    
    def __init__(self, name, email, phone, address=None):
        """Initialize a guest"""
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
        self._bookings = []
        self._loyalty_program = None
        self._registration_date = datetime.now()
    
    # getters
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
    
    def get_phone(self):
        return self._phone
    
    def get_address(self):
        return self._address
    
    def get_bookings(self):
        return self._bookings
    
    def get_loyalty_program(self):
        return self._loyalty_program
    
    def get_registration_date(self):
        return self._registration_date
    
    # setters
    def set_name(self, name):
        self._name = name
    
    def set_email(self, email):
        self._email = email
    
    def set_phone(self, phone):
        self._phone = phone
    
    def set_address(self, address):
        self._address = address
    
    def add_booking(self, booking):
        """Add a booking to the guest's history"""
        self._bookings.append(booking)
    
    def enroll_in_loyalty_program(self):
        if not self._loyalty_program:
            self._loyalty_program = LoyaltyProgram()
        return self._loyalty_program
    
    def __str__(self):
        return (f"Guest: {self._name}\n"
                f"Email: {self._email}\n"
                f"Phone: {self._phone}\n"
                f"Member Since: {self._registration_date.strftime('%Y-%m-%d')}\n"
                f"Loyalty Program: {'Enrolled' if self._loyalty_program else 'Not Enrolled'}")

class LoyaltyProgram:
    """Class representing the hotel's loyalty program"""
    
    def __init__(self):
        self._points = 0
        self._tier = "Basic"
        self._free_nights_earned = 0
    
    def get_points(self):
        return self._points
    
    def get_tier(self):
        return self._tier
    
    def get_free_nights_earned(self):
        return self._free_nights_earned
    
    def add_points(self, points):
        """Add points to the loyalty account"""
        self._points += points
        self._update_tier()
    
    def redeem_points(self, points):
        """Redeem points for rewards"""
        if points > self._points:
            raise ValueError("Not enough points to redeem")
        self._points -= points
        self._update_tier()
    
    def _update_tier(self):
        """Update the loyalty tier based on points"""
        if self._points >= 1000:
            self._tier = "Gold"
        elif self._points >= 500:
            self._tier = "Silver"
        else:
            self._tier = "Basic"
    
    def earn_free_night(self):
        """Earn a free night when enough points are accumulated"""
        if self._points >= 200:
            self._points -= 200
            self._free_nights_earned += 1
            return True
        return False
    
    def set_points(self, points):
        self._points = points
        self._update_tier()
    
    def set_tier(self, tier):
        self._tier = tier
    
    def set_free_nights_earned(self, free_nights):
        self._free_nights_earned = free_nights
    
    def __str__(self):
        return (f"Loyalty Status: {self._tier}\n"
                f"Points: {self._points}\n"
                f"Free Nights Earned: {self._free_nights_earned}")