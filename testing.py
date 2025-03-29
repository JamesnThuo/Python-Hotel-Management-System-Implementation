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
    print("Example 1: Basic account creation")
    new_guest1 = hotel.register_guest(
        "Alice Wonderland",
        "alice@example.com",
        "555-0123"
    )
    print("New Guest Created:")
    print(new_guest1)
    
    print("\nExample 2: Account with full details")
    new_guest2 = hotel.register_guest(
        "Bob Builder",
        "bob@example.com",
        "555-0124",
        "123 Construction St"
    )
    print("New Guest with Address Created:")
    print(new_guest2)
    print("\n" + "="*50 + "\n")
    
    # Test Case 2: Searching for Available Rooms
    print("TEST CASE 2: Searching for Available Rooms")
    print("Example 1: All available rooms")
    available_rooms = hotel.find_available_rooms()
    print(f"Found {len(available_rooms)} available rooms:")
    for room in available_rooms[:2]:  # Display first 2 for brevity
        print(room)
        print("-" * 20)
    
    print("\nExample 2: Filter by room type")
    deluxe_rooms = hotel.find_available_rooms(room_type="Deluxe")
    print(f"Found {len(deluxe_rooms)} deluxe rooms:")
    for room in deluxe_rooms:
        print(room)
        print("-" * 20)
    print("\n" + "="*50 + "\n")
    
    # Test Case 3: Making a Room Reservation
    print("TEST CASE 3: Making a Room Reservation")
    check_in = datetime.now().date() + timedelta(days=7)
    check_out = check_in + timedelta(days=3)
    
    print("Example 1: Successful booking")
    guest = hotel.get_guests()[0]  # Use John Doe
    room = hotel.get_rooms()[2]    # Use Deluxe Room 201
    print(f"Booking for {guest.get_name()} in Room {room.get_room_number()}")
    booking1 = hotel.create_booking(guest, room, check_in, check_out)
    print("Booking Created:")
    print(booking1)
    
    print("\nExample 2: Attempt to book unavailable room")
    try:
        booking2 = hotel.create_booking(guest, room, check_in, check_out)
    except ValueError as e:
        print(f"Expected Error: {str(e)}")
    print("\n" + "="*50 + "\n")
    
    # Test Case 4: Invoice Generation
    print("TEST CASE 4: Invoice Generation")
    print("Example 1: Basic invoice")
    invoice1 = booking1.generate_invoice()
    print("Invoice Generated:")
    print(invoice1)
    
    print("\nExample 2: Invoice after adding services")
    hotel.add_service_request(booking1, 'roomservice', {'items': ['Burger', 'Fries']})
    invoice2 = booking1.generate_invoice()
    print("Updated Invoice:")
    print(invoice2)
    print("\n" + "="*50 + "\n")
    
    # Test Case 5: Processing Different Payment Methods
    print("TEST CASE 5: Processing Different Payment Methods")
    
    print("Example 1: Credit Card Payment")
    credit_payment = hotel.process_payment(
        booking1,
        'credit',
        {
            'card_number': '4111111111111111',
            'card_holder': guest.get_name(),
            'expiry_date': '12/25',
            'cvv': '123'
        }
    )
    print(credit_payment)
    
    print("\nExample 2: Mobile Wallet Payment")
    guest2 = hotel.get_guests()[1]  # Jane Smith
    room2 = hotel.get_rooms()[3]    # Deluxe Room 202
    booking2 = hotel.create_booking(guest2, room2, check_in, check_out)
    mobile_payment = hotel.process_payment(
        booking2,
        'mobile',
        {
            'wallet_type': 'Apple Pay',
            'phone_number': guest2.get_phone()
        }
    )
    print(mobile_payment)
    print("\n" + "="*50 + "\n")
    
    # Test Case 6: Displaying Reservation History
    print("TEST CASE 6: Displaying Reservation History")
    print(f"Example 1: {guest.get_name()}'s Reservations")
    print(f"Reservation History for {guest.get_name()}:")
    for idx, booking in enumerate(guest.get_bookings(), 1):
        print(f"\nBooking {idx}:")
        print(booking)
    
    print(f"\nExample 2: {guest2.get_name()}'s Reservations")
    print(f"Reservation History for {guest2.get_name()}:")
    for idx, booking in enumerate(guest2.get_bookings(), 1):
        print(f"\nBooking {idx}:")
        print(booking)
    print("\n" + "="*50 + "\n")
    
    # Test Case 7: Cancellation of a Reservation
    print("TEST CASE 7: Cancellation of a Reservation")
    print("Example 1: Successful cancellation")
    guest3 = hotel.get_guests()[2]  # Robert Johnson
    room3 = hotel.get_rooms()[1]    # Standard Room 102
    booking3 = hotel.create_booking(guest3, room3, check_in, check_out)
    print("Booking before cancellation:")
    print(booking3)
    print(f"Room available before cancellation: {room3.is_available()}")
    
    booking3.cancel_booking()
    print("\nAfter cancellation:")
    print(booking3)
    print(f"Room available after cancellation: {room3.is_available()}")
    
    print("\nExample 2: Attempt to cancel already cancelled booking")
    try:
        booking3.cancel_booking()
    except Exception as e:
        print(f"Expected Error: {str(e)}")
    print("\n" + "="*50 + "\n")
    
    # Test Case 8: Loyalty Program Operations
    print("TEST CASE 8: Loyalty Program Operations")
    guest = hotel.get_guests()[0]  # John Doe (already has 300 points)
    loyalty = guest.get_loyalty_program()
    print(f"Example 1: Current loyalty status for {guest.get_name()}:")
    print(loyalty)
    
    print("\nAdding 200 points:")
    loyalty.add_points(200)
    print(loyalty)
    
    print("\nExample 2: Redeeming points")
    print("Redeeming 100 points:")
    loyalty.redeem_points(100)
    print(loyalty)
    
    print("\nAttempting to earn free night:")
    if loyalty.earn_free_night():
        print("Earned a free night!")
        print(loyalty)
    print("\n" + "="*50 + "\n")
    
    # Test Case 9: Guest Services and Requests
    print("TEST CASE 9: Guest Services and Requests")
    print("Example 1: Housekeeping service")
    housekeeping = hotel.add_service_request(
        booking1,
        'housekeeping',
        {'service_type': 'Deep'}
    )
    print(housekeeping)
    
    print("\nExample 2: Transportation service")
    transportation = hotel.add_service_request(
        booking1,
        'transportation',
        {'vehicle_type': 'SUV', 'destination': 'Airport'}
    )
    print(transportation)
    
    print("\nUpdated Invoice with Services:")
    print(booking1.generate_invoice())
    print("\n" + "="*50 + "\n")
    
    # Test Case 10: Feedback and Reviews
    print("TEST CASE 10: Feedback and Reviews")
    print("Example 1: Submitting feedback")
    feedback1 = hotel.submit_feedback(
        guest,
        5,
        "Excellent stay! The room was clean and comfortable.",
        check_in
    )
    print("Guest Feedback:")
    print(feedback1)
    
    print("\nExample 2: Feedback with management response")
    feedback1.add_response("Thank you for your kind words! We hope to see you again soon.")
    print("Feedback with Response:")
    print(feedback1)
    
    print("\nExample 3: Attempt to submit invalid rating")
    try:
        feedback2 = hotel.submit_feedback(guest, 6, "Too good to be true")
    except ValueError as e:
        print(f"Expected Error: {str(e)}")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()