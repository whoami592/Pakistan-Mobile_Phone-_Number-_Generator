import random

def generate_pak_number():
    # Pakistani mobile numbers start with +92 followed by 3 and then 9 digits
    operators = ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39']  # Common operator codes
    operator = random.choice(operators)
    subscriber = ''.join([str(random.randint(0, 9)) for _ in range(7)])  # 7 random digits
    return f"+92{operator}{subscriber}"

def create_number_database(count):
    database = []
    for _ in range(count):
        number = generate_pak_number()
        database.append({
            'phone_number': number,
            'status': 'active'  # You can add more fields as needed
        })
    return database

# Generate 10 sample numbers
if __name__ == "__main__":
    number_of_entries = 10
    pak_numbers = create_number_database(number_of_entries)
    
    # Print the database
    for entry in pak_numbers:
        print(f"Number: {entry['phone_number']}, Status: {entry['status']}")
        