from datetime import datetime

class Feedback:
    """Class representing guest feedback"""
    
    def __init__(self, guest, rating, comments, stay_date=None):
        """Initialize feedback"""
        self._guest = guest
        self._rating = rating
        self._comments = comments
        self._date = datetime.now().date()
        self._stay_date = stay_date if stay_date else self._date
        self._response = None
    
    # getters
    def get_guest(self):
        return self._guest
    
    def get_rating(self):
        return self._rating
    
    def get_comments(self):
        return self._comments
    
    def get_date(self):
        return self._date
    
    def get_stay_date(self):
        return self._stay_date
    
    def get_response(self):
        return self._response
    
    # Setters
    def set_guest(self, guest):
        self._guest = guest
    
    def set_rating(self, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = rating
    
    def set_comments(self, comments):
        self._comments = comments
    
    def set_response(self, response_text):
        self._response = response_text
    
    def add_response(self, response_text):
        self._response = response_text
    
    def __str__(self):
        feedback_str = (f"Feedback from {self._guest.get_name()}\n"
                       f"Stay Date: {self._stay_date}\n"
                       f"Rating: {'★' * self._rating}{'☆' * (5 - self._rating)}\n"
                       f"Comments: {self._comments}")
        
        if self._response:
            feedback_str += f"\n\nManagement Response:\n{self._response}"
        
        return feedback_str