class Payment:
    """Base class for payment methods"""
    
    def __init__(self, amount, payment_date):
        """Initialize a payment"""
        self._amount = amount
        self._payment_date = payment_date
        self._status = "Pending"
        self._transaction_id = None
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def payment_date(self):
        return self._payment_date
    
    @property
    def status(self):
        return self._status
    
    @property
    def transaction_id(self):
        return self._transaction_id
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    def process_payment(self):
        """Process the payment (to be implemented by subclasses)"""
        raise NotImplementedError
    
    def __str__(self):
        return (f"Payment Amount: ${self._amount:.2f}\n"
                f"Date: {self._payment_date}\n"
                f"Status: {self._status}")


class CreditCardPayment(Payment):
    """Credit card payment method"""
    
    def __init__(self, amount, payment_date, card_number, card_holder, expiry_date, cvv):
        """Initialize a credit card payment"""
        super().__init__(amount, payment_date)
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvv = cvv
    
    @property
    def card_number(self):
        return self._card_number
    
    @property
    def card_holder(self):
        return self._card_holder
    
    @property
    def expiry_date(self):
        return self._expiry_date
    
    @property
    def cvv(self):
        return self._cvv
    
    def process_payment(self):
        """Process the credit card payment"""
        self._transaction_id = f"CC-{self._payment_date.strftime('%Y%m%d%H%M%S')}"
        self._status = "Completed"
        return True
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Payment Method: Credit Card\n"
                f"Card Holder: {self._card_holder}\n"
                f"Last 4 Digits: **** **** **** {self._card_number[-4:]}")


class DebitCardPayment(Payment):
    """Debit card payment method"""
    
    def __init__(self, amount, payment_date, card_number, card_holder, expiry_date, cvv):
        """Initialize a debit card payment"""
        super().__init__(amount, payment_date)
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvv = cvv
    
    @property
    def card_number(self):
        return self._card_number
    
    @property
    def card_holder(self):
        return self._card_holder
    
    @property
    def expiry_date(self):
        return self._expiry_date
    
    @property
    def cvv(self):
        return self._cvv
    
    def process_payment(self):
        """Process the debit card payment"""
        self._transaction_id = f"DC-{self._payment_date.strftime('%Y%m%d%H%M%S')}"
        self._status = "Completed"
        return True
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Payment Method: Debit Card\n"
                f"Card Holder: {self._card_holder}\n"
                f"Last 4 Digits: **** **** **** {self._card_number[-4:]}")


class MobileWalletPayment(Payment):
    """Mobile wallet payment method"""
    
    def __init__(self, amount, payment_date, wallet_type, phone_number):
        """Initialize a mobile wallet payment"""
        super().__init__(amount, payment_date)
        self._wallet_type = wallet_type
        self._phone_number = phone_number
    
    @property
    def wallet_type(self):
        return self._wallet_type
    
    @property
    def phone_number(self):
        return self._phone_number
    
    def process_payment(self):
        """Process the mobile wallet payment"""
        # In a real system, this would connect to a payment gateway
        # For this example, we'll simulate a successful payment
        self._transaction_id = f"MW-{self._payment_date.strftime('%Y%m%d%H%M%S')}"
        self._status = "Completed"
        return True
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Payment Method: {self._wallet_type}\n"
                f"Phone Number: {self._phone_number}")