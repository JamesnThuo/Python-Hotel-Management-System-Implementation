from datetime import datetime, timedelta
from hotel_system import HotelSystem

def main():
    # Initialize the hotel system
    hotel = HotelSystem()
    print("Hotel System Initialized")
    print(hotel)
    print("\n" + "="*50 + "\n")
    
    # Test Case 1: Guest Account Creation
    print("TEST CASE 1: Guest Account Creation")
    new_guest = hotel.register_guest(
        "Alice Wonderland",
        "alice@example.com",
        "555-0123",
        "123 Wonder St, Fantasyland"
    )
    print("New Guest Created:")
    print(new_guest)
    print("\n" + "="*50 + "\n")
    
    # Test Case 2: Searching for Available Rooms
    print("TEST CASE 2: Searching for Available Rooms")
    available_rooms = hotel.find_available_rooms()
    print("All Available Rooms:")
    for room in available_rooms:
        print(room)
        print("-" * 20)
    
    deluxe_rooms = hotel.find_available_rooms(room_type="Deluxe")
    print("\nAvailable Deluxe Rooms:")
    for room in deluxe_rooms:
        print(room)
        print("-" * 20)
    print("\n" + "="*50 + "\n")
    
    # Test Case 3: Making a Room Reservation
    print("TEST CASE 3: Making a Room Reservation")
    check_in = datetime.now().date() + timedelta(days=7)
    check_out = check_in + timedelta(days=3)
    
    # Get a guest and room for booking
    guest = hotel.guests[0]  # Use John Doe
    room = hotel.rooms[2]    # Use Deluxe Room 201
    
    print(f"Booking for {guest.name} in Room {room.room_number}")
    booking = hotel.create_booking(guest, room, check_in, check_out)
    print("Booking Created:")
    print(booking)
    print("\n" + "="*50 + "\n")
    
    # Test Case 4: Invoice Generation
    print("TEST CASE 4: Invoice Generation")
    invoice = booking.generate_invoice()
    print("Invoice Generated:")
    print(invoice)
    print("\n" + "="*50 + "\n")
    
    # Test Case 5: Processing Different Payment Methods
    print("TEST CASE 5: Processing Different Payment Methods")
    
    # Credit Card Payment
    print("Credit Card Payment:")
    credit_payment = hotel.process_payment(
        booking,
        'credit',
        {
            'card_number': '4111111111111111',
            'card_holder': 'John Doe',
            'expiry_date': '12/25',
            'cvv': '123'
        }
    )
    print(credit_payment)
    
    # Mobile Wallet Payment (for a different booking)
    print("\nMobile Wallet Payment:")
    guest2 = hotel.guests[1]  # Jane Smith
    room2 = hotel.rooms[3]    # Deluxe Room 202
    booking2 = hotel.create_booking(guest2, room2, check_in, check_out)
    mobile_payment = hotel.process_payment(
        booking2,
        'mobile',
        {
            'wallet_type': 'Apple Pay',
            'phone_number': '555-0102'
        }
    )
    print(mobile_payment)
    print("\n" + "="*50 + "\n")
    
    # Test Case 6: Displaying Reservation History
    print("TEST CASE 6: Displaying Reservation History")
    print(f"Reservation History for {guest.name}:")
    for idx, booking in enumerate(guest.bookings, 1):
        print(f"\nBooking {idx}:")
        print(booking)
    print("\n" + "="*50 + "\n")
    
    # Test Case 7: Cancellation of a Reservation
    print("TEST CASE 7: Cancellation of a Reservation")
    guest3 = hotel.guests[2]  # Robert Johnson
    room3 = hotel.rooms[1]    # Standard Room 102
    booking3 = hotel.create_booking(guest3, room3, check_in, check_out)
    print("Booking before cancellation:")
    print(booking3)
    print(f"Room available before cancellation: {room3.is_available}")
    
    booking3.cancel_booking()
    print("\nAfter cancellation:")
    print(booking3)
    print(f"Room available after cancellation: {room3.is_available}")
    print("\n" + "="*50 + "\n")
    
    # Test Case 8: Loyalty Program Operations
    print("TEST CASE 8: Loyalty Program Operations")
    guest = hotel.guests[0]  # John Doe (already has 300 points)
    loyalty = guest.loyalty_program
    print(f"Current loyalty status for {guest.name}:")
    print(loyalty)
    
    # Add more points
    loyalty.add_points(200)
    print("\nAfter adding 200 points:")
    print(loyalty)
    
    # Redeem points
    loyalty.redeem_points(100)
    print("\nAfter redeeming 100 points:")
    print(loyalty)
    
    # Earn free night
    if loyalty.earn_free_night():
        print("\nEarned a free night!")
        print(loyalty)
    print("\n" + "="*50 + "\n")
    
    # Test Case 9: Guest Services and Requests
    print("TEST CASE 9: Guest Services and Requests")
    
    # Housekeeping service
    print("Housekeeping Service:")
    housekeeping = hotel.add_service_request(
        booking,
        'housekeeping',
        {'service_type': 'Deep'}
    )
    print(housekeeping)
    
    # Room service
    print("\nRoom Service:")
    room_service = hotel.add_service_request(
        booking,
        'roomservice',
        {'items': ['Cheeseburger', 'Fries', 'Soda']}
    )
    print(room_service)
    
    # Updated invoice
    print("\nUpdated Invoice with Services:")
    print(booking.generate_invoice())
    print("\n" + "="*50 + "\n")
    
    # Test Case 10: Feedback and Reviews
    print("TEST CASE 10: Feedback and Reviews")
    feedback = hotel.submit_feedback(
        guest,
        5,
        "Excellent stay! The room was clean and comfortable.",
        check_in
    )
    print("Guest Feedback:")
    print(feedback)
    
    # Add management response
    feedback.add_response("Thank you for your kind words! We hope to see you again soon.")
    print("\nFeedback with Response:")
    print(feedback)

if __name__ == "__main__":
    main()