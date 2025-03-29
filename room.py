class Room:
    """Base class for all room types in the hotel"""
    
    def __init__(self, room_number, room_type, amenities, price_per_night, is_available=True):
        """Initialize a room"""
        self._room_number = room_number
        self._room_type = room_type
        self._amenities = amenities
        self._price_per_night = price_per_night
        self._is_available = is_available
    
    # Getters
    def room_number(self):
        return self._room_number
    
    def get_room_type(self):
        return self._room_type
    
    def get_amenities(self):
        return self._amenities
    
    def get_price_per_night(self):
        return self._price_per_night
    
    def is_available(self):
        return self._is_available
    
    # setters
    def set_room_number(self, room_number):
        self._room_number = room_number
    
    def set_room_type(self, room_type):
        self._room_type = room_type
    
    def set_amenities(self, amenities):
        self._amenities = amenities
    
    def set_price_per_night(self, price_per_night):
        self._price_per_night = price_per_night
    
    def set_available(self, is_available):
        self._is_available = is_available
    
    def __str__(self):
        return (f"Room {self._room_number} - {self._room_type}\n"
                f"Amenities: {', '.join(self._amenities)}\n"
                f"Price per night: ${self._price_per_night:.2f}\n"
                f"Available: {'Yes' if self._is_available else 'No'}")

class StandardRoom(Room):
    """Standard room type with basic amenities"""
    
    def __init__(self, room_number, price_per_night, is_available=True):
        amenities = ["Wi-Fi", "Television", "Air Conditioning"]
        super().__init__(room_number, "Standard", amenities, price_per_night, is_available)
        self._max_occupancy = 2
        self._has_balcony = False
    
    def get_max_occupancy(self):
        return self._max_occupancy
    
    def has_balcony(self):
        return self._has_balcony
    
    def set_max_occupancy(self, max_occupancy):
        self._max_occupancy = max_occupancy
    
    def set_has_balcony(self, has_balcony):
        self._has_balcony = has_balcony
    
    def __str__(self):
        return super().__str__() + f"\nMax Occupancy: {self._max_occupancy}"

class DeluxeRoom(Room):
    """Deluxe room type with additional amenities"""
    
    def __init__(self, room_number, price_per_night, is_available=True):
        amenities = ["Wi-Fi", "Television", "Air Conditioning", "Mini-Bar", "Coffee Maker"]
        super().__init__(room_number, "Deluxe", amenities, price_per_night, is_available)
        self._max_occupancy = 4
        self._has_balcony = True
    
    def get_max_occupancy(self):
        return self._max_occupancy
    
    def has_balcony(self):
        return self._has_balcony
    
    def set_max_occupancy(self, max_occupancy):
        self._max_occupancy = max_occupancy
    
    def set_has_balcony(self, has_balcony):
        self._has_balcony = has_balcony
    
    def __str__(self):
        return super().__str__() + f"\nMax Occupancy: {self._max_occupancy}\nBalcony: {'Yes' if self._has_balcony else 'No'}"

class Suite(Room):
    """Suite room type with premium amenities"""
    
    def __init__(self, room_number, price_per_night, is_available=True):
        amenities = ["Wi-Fi", "Television", "Air Conditioning", "Mini-Bar", 
                    "Coffee Maker", "Jacuzzi", "Living Area"]
        super().__init__(room_number, "Suite", amenities, price_per_night, is_available)
        self._max_occupancy = 6
        self._has_balcony = True
        self._separate_bedroom = True
    
    def get_max_occupancy(self):
        return self._max_occupancy
    
    def has_balcony(self):
        return self._has_balcony
    
    def has_separate_bedroom(self):
        return self._separate_bedroom
    
    def set_max_occupancy(self, max_occupancy):
        self._max_occupancy = max_occupancy
    
    def set_has_balcony(self, has_balcony):
        self._has_balcony = has_balcony
    
    def set_separate_bedroom(self, separate_bedroom):
        self._separate_bedroom = separate_bedroom
    
    def __str__(self):
        return (super().__str__() + 
                f"\nMax Occupancy: {self._max_occupancy}\n"
                f"Balcony: {'Yes' if self._has_balcony else 'No'}\n"
                f"Separate Bedroom: {'Yes' if self._separate_bedroom else 'No'}")