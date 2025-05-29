import hashlib
import os
import string
import random

class PasswordManager:
    """Handles password hashing and verification."""

    @staticmethod
    def hash_password(password: str, salt: bytes = None) -> tuple:
        """Hash a password with a random salt using SHA-256."""
        if salt is None:
            salt = os.urandom(16)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt, pwd_hash

    @staticmethod
    def verify_password(password: str, salt: bytes, pwd_hash: bytes) -> bool:
        """Verify a password against the given salt and hash."""
        check_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return check_hash == pwd_hash

    @staticmethod
    def generate_password(length=12) -> str:
        """Generate a random password of given length."""
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    choice = input("Do you want to enter your own password? (y/n/a for auto-generate): ").strip().lower()
    if choice == 'y':
        password = input("Enter a password to hash: ")
    elif choice == 'a':
        password = PasswordManager.generate_password()
        print(f"Auto-generated password: {password}")
    else:
        password = PasswordManager.generate_password()
        print(f"Generated password: {password}")

    salt, pwd_hash = PasswordManager.hash_password(password)
    print(f"Salt: {salt.hex()}")
    print(f"Hash: {pwd_hash.hex()}")

    check = input("Re-enter password to verify: ")
    if PasswordManager.verify_password(check, salt, pwd_hash):
        print("Password is correct!")
    else:
        print("Password is incorrect.")