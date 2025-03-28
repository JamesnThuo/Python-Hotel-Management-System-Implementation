class ServiceRequest:
    """Base class for service requests"""
    
    def __init__(self, request_date, room, description):
        """Initialize a service request"""
        self._request_date = request_date
        self._room = room
        self._description = description
        self._status = "Pending"
        self._price = 0
    
    @property
    def request_date(self):
        return self._request_date
    
    @property
    def room(self):
        return self._room
    
    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status
    
    @property
    def price(self):
        return self._price
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    def complete_service(self):
        """Mark the service as completed"""
        self._status = "Completed"
    
    def __str__(self):
        return (f"Service Request for Room {self._room.room_number}\n"
                f"Type: {self.__class__.__name__}\n"
                f"Description: {self._description}\n"
                f"Status: {self._status}\n"
                f"Price: ${self._price:.2f}")


class Housekeeping(ServiceRequest):
    """Housekeeping service request"""
    
    def __init__(self, request_date, room, service_type="Standard"):
        """Initialize a housekeeping request"""
        description = f"{service_type} Cleaning"
        super().__init__(request_date, room, description)
        self._service_type = service_type
        self._set_price()
    
    @property
    def service_type(self):
        return self._service_type
    
    def _set_price(self):
        """Set price based on service type"""
        if self._service_type == "Standard":
            self._price = 0 
        elif self._service_type == "Deep":
            self._price = 25.00
        elif self._service_type == "Eco":
            self._price = 15.00
    
    def __str__(self):
        return super().__str__()


class RoomService(ServiceRequest):
    """Room service request"""
    
    def __init__(self, request_date, room, items):
        """Initialize a room service request"""
        description = "Room Service Order"
        super().__init__(request_date, room, description)
        self._items = items
        self._calculate_price()
    
    @property
    def items(self):
        return self._items
    
    def _calculate_price(self):
        """Calculate price based on ordered items"""
        self._price = len(self._items) * 12.50  
    
    def __str__(self):
        items_str = "\n".join(f"- {item}" for item in self._items)
        return (super().__str__() + "\n"
                f"Items Ordered:\n{items_str}")


class Transportation(ServiceRequest):
    """Transportation service request"""
    
    def __init__(self, request_date, room, vehicle_type, destination):
        """Initialize a transportation request"""
        description = f"{vehicle_type} to {destination}"
        super().__init__(request_date, room, description)
        self._vehicle_type = vehicle_type
        self._destination = destination
        self._set_price()
    
    @property
    def vehicle_type(self):
        return self._vehicle_type
    
    @property
    def destination(self):
        return self._destination
    
    def _set_price(self):
        """Set price based on vehicle type"""
        if self._vehicle_type == "Sedan":
            self._price = 35.00
        elif self._vehicle_type == "SUV":
            self._price = 50.00
        elif self._vehicle_type == "Limo":
            self._price = 100.00
    
    def __str__(self):
        return super().__str__()