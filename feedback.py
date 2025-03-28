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
    
    @property
    def guest(self):
        return self._guest
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def comments(self):
        return self._comments
    
    @property
    def date(self):
        return self._date
    
    @property
    def stay_date(self):
        return self._stay_date
    
    @property
    def response(self):
        return self._response
    
    def add_response(self, response_text):
        """Add a management response to the feedback"""
        self._response = response_text
    
    def __str__(self):
        feedback_str = (f"Feedback from {self._guest.name}\n"
                       f"Stay Date: {self._stay_date}\n"
                       f"Rating: {'★' * self._rating}{'☆' * (5 - self._rating)}\n"
                       f"Comments: {self._comments}")
        
        if self._response:
            feedback_str += f"\n\nManagement Response:\n{self._response}"
        
        return feedback_str