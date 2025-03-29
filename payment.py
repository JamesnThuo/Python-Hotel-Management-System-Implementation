class Payment:
    """Base class for payment methods"""
    
    def __init__(self, amount, payment_date):
        """Initialize a payment"""
        self._amount = amount
        self._payment_date = payment_date
        self._status = "Pending"
        self._transaction_id = None
    
    def get_amount(self):
        return self._amount
    
    def get_payment_date(self):
        return self._payment_date
    
    def get_status(self):
        return self._status
    
    def get_transaction_id(self):
        return self._transaction_id
    
    def set_amount(self, amount):
        self._amount = amount
    
    def set_payment_date(self, payment_date):
        self._payment_date = payment_date
    
    def set_status(self, status):
        self._status = status
    
    def process_payment(self):
        raise NotImplementedError
    
    def __str__(self):
        return (f"Payment Amount: ${self._amount:.2f}\n"
                f"Date: {self._payment_date}\n"
                f"Status: {self._status}")

class CreditCardPayment(Payment):
    """Credit card payment method"""
    
    def __init__(self, amount, payment_date, card_number, card_holder, expiry_date, cvv):
        super().__init__(amount, payment_date)
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvv = cvv
    
    def get_card_number(self):
        return self._card_number
    
    def get_card_holder(self):
        return self._card_holder
    
    def get_expiry_date(self):
        return self._expiry_date
    
    def get_cvv(self):
        return self._cvv
    
    def set_card_number(self, card_number):
        self._card_number = card_number
    
    def set_card_holder(self, card_holder):
        self._card_holder = card_holder
    
    def set_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
    
    def set_cvv(self, cvv):
        self._cvv = cvv
    
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
        super().__init__(amount, payment_date)
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvv = cvv
    
    def get_card_number(self):
        return self._card_number
    
    def get_card_holder(self):
        return self._card_holder
    
    def get_expiry_date(self):
        return self._expiry_date
    
    def get_cvv(self):
        return self._cvv
    
    def set_card_number(self, card_number):
        self._card_number = card_number
    
    def set_card_holder(self, card_holder):
        self._card_holder = card_holder
    
    def set_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
    
    def set_cvv(self, cvv):
        self._cvv = cvv
    
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
        super().__init__(amount, payment_date)
        self._wallet_type = wallet_type
        self._phone_number = phone_number
    
    def get_wallet_type(self):
        return self._wallet_type
    
    def get_phone_number(self):
        return self._phone_number
    
    def set_wallet_type(self, wallet_type):
        self._wallet_type = wallet_type
    
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
    
    def process_payment(self):
        """Process the mobile wallet payment"""
        self._transaction_id = f"MW-{self._payment_date.strftime('%Y%m%d%H%M%S')}"
        self._status = "Completed"
        return True
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Payment Method: {self._wallet_type}\n"
                f"Phone Number: {self._phone_number}")