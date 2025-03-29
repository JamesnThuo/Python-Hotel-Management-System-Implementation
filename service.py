class ServiceRequest:
    def __init__(self, request_date, room, description):
        self._request_date = request_date
        self._room = room
        self._description = description
        self._status = "Pending"
        self._price = 0
    
    def get_request_date(self):
        return self._request_date
    
    def get_room(self):
        return self._room
    
    def get_description(self):
        return self._description
    
    def get_status(self):
        return self._status
    
    def get_price(self):
        return self._price
    
    def set_request_date(self, request_date):
        self._request_date = request_date
    
    def set_room(self, room):
        self._room = room
    
    def set_description(self, description):
        self._description = description
    
    def set_status(self, status):
        self._status = status
    
    def set_price(self, price):
        self._price = price
    
    def complete_service(self):
        self._status = "Completed"
    
    def __str__(self):
        return (f"Service Request for Room {self._room.get_room_number()}\n"
                f"Type: {self.__class__.__name__}\n"
                f"Description: {self._description}\n"
                f"Status: {self._status}\n"
                f"Price: ${self._price:.2f}")

class Housekeeping(ServiceRequest):
    def __init__(self, request_date, room, service_type="Standard"):
        description = f"{service_type} Cleaning"
        super().__init__(request_date, room, description)
        self._service_type = service_type
        self._set_price()
    
    def get_service_type(self):
        return self._service_type
    
    def set_service_type(self, service_type):
        self._service_type = service_type
        self._set_price()
    
    def _set_price(self):
        if self._service_type == "Standard":
            self._price = 0
        elif self._service_type == "Deep":
            self._price = 25.00
        elif self._service_type == "Eco":
            self._price = 15.00
    
    def __str__(self):
        return super().__str__()

class RoomService(ServiceRequest):
    def __init__(self, request_date, room, items):
        description = "Room Service Order"
        super().__init__(request_date, room, description)
        self._items = items
        self._calculate_price()
    
    def get_items(self):
        return self._items
    
    def set_items(self, items):
        self._items = items
        self._calculate_price()
    
    def _calculate_price(self):
        self._price = len(self._items) * 12.50
    
    def __str__(self):
        items_str = "\n".join(f"- {item}" for item in self._items)
        return (super().__str__() + "\n"
                f"Items Ordered:\n{items_str}")

class Transportation(ServiceRequest):
    def __init__(self, request_date, room, vehicle_type, destination):
        description = f"{vehicle_type} to {destination}"
        super().__init__(request_date, room, description)
        self._vehicle_type = vehicle_type
        self._destination = destination
        self._set_price()
    
    def get_vehicle_type(self):
        return self._vehicle_type
    
    def get_destination(self):
        return self._destination
    
    def set_vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type
        self._set_price()
    
    def set_destination(self, destination):
        self._destination = destination
    
    def _set_price(self):
        if self._vehicle_type == "Sedan":
            self._price = 35.00
        elif self._vehicle_type == "SUV":
            self._price = 50.00
        elif self._vehicle_type == "Limo":
            self._price = 100.00
    
    def __str__(self):
        return super().__str__()