import random
import string
import hashlib
import os

def random_string(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_phone_number():
    """Generate a random phone number in the format (XXX) XXX-XXXX."""
    return f"({random.randint(100,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}"

def random_email(name=None):
    """Generate a random email address. Optionally use a name as the prefix."""
    domains = ['example.com', 'testmail.com', 'mailinator.com']
    prefix = name if name else random_string(6).lower()
    return f"{prefix}@{random.choice(domains)}"

def hash_password(password: str, salt: bytes = None) -> tuple:
    """Hash a password with a random salt using SHA-256."""
    if salt is None:
        salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, pwd_hash

def verify_password(password: str, salt: bytes, pwd_hash: bytes) -> bool:
    """Verify a password against the given salt and hash."""
    check_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return check_hash == pwd_hash

def generate_password(length=12) -> str:
    """Generate a random password of given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def input_contact():
    """Prompt the user to input contact details."""
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    set_password = input("Do you want to set a password for this contact? (y/n/a for auto-generate/b for both): ").strip().lower()
    if set_password == 'y':
        password = input("Enter password: ")
        salt, pwd_hash = hash_password(password)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password_salt": salt.hex(),
            "password_hash": pwd_hash.hex(),
            "auto_password": None
        }
    elif set_password == 'a':
        password = generate_password()
        print(f"Auto-generated password: {password}")
        salt, pwd_hash = hash_password(password)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password_salt": salt.hex(),
            "password_hash": pwd_hash.hex(),
            "auto_password": password
        }
    elif set_password == 'b':
        password = input("Enter your password: ")
        auto_password = generate_password()
        print(f"Auto-generated password: {auto_password}")
        salt, pwd_hash = hash_password(password)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password_salt": salt.hex(),
            "password_hash": pwd_hash.hex(),
            "auto_password": auto_password
        }
    else:
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password_salt": None,
            "password_hash": None,
            "auto_password": None
        }

def input_contacts(n=1):
    """Prompt the user to input n contacts."""
    return [input_contact() for _ in range(n)]

def access_contact(contact):
    """Prompt for password if contact is password-protected, then display contact info if correct."""
    if contact.get("password_hash") and contact.get("password_salt"):
        password = input("Enter password to access this contact: ")
        salt = bytes.fromhex(contact["password_salt"])
        pwd_hash = bytes.fromhex(contact["password_hash"])
        if verify_password(password, salt, pwd_hash):
            print(f"Access granted: {contact}")
            if contact.get("auto_password"):
                print(f"Auto-generated password for this contact: {contact['auto_password']}")
        else:
            print("Access denied: Incorrect password.")
    else:
        print(f"Access granted: {contact}")

if __name__ == "__main__":
    try:
        num = int(input("How many contacts do you want to enter? "))
        contacts = input_contacts(num)
        print("\nContacts entered:")
        for idx, contact in enumerate(contacts, 1):
            print(f"\nContact {idx}:")
            access_contact(contact)
    except ValueError:
        print("Please enter a valid number.")