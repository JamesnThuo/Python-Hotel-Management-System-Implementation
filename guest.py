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
    
    # Getters
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        return self._phone
    
    @property
    def address(self):
        return self._address
    
    @property
    def bookings(self):
        return self._bookings
    
    @property
    def loyalty_program(self):
        return self._loyalty_program
    
    @property
    def registration_date(self):
        return self._registration_date
    
    # Setters
    @email.setter
    def email(self, new_email):
        self._email = new_email
    
    @phone.setter
    def phone(self, new_phone):
        self._phone = new_phone
    
    @address.setter
    def address(self, new_address):
        self._address = new_address
    
    def add_booking(self, booking):
        """Add a booking to the guest's history"""
        self._bookings.append(booking)
    
    def enroll_in_loyalty_program(self):
        """Enroll the guest in the loyalty program"""
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
    
    @property
    def points(self):
        return self._points
    
    @property
    def tier(self):
        return self._tier
    
    @property
    def free_nights_earned(self):
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
    
    def __str__(self):
        return (f"Loyalty Status: {self._tier}\n"
                f"Points: {self._points}\n"
                f"Free Nights Earned: {self._free_nights_earned}")