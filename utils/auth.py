# utils/auth.py

def login():
    print("\n🔐 Admin Login Required")
    username = input("Username: ")
    password = input("Password: ")

    # Hardcoded credentials (can be upgraded to hashed passwords)
    if username == "admin" and password == "1234":
        print("✅ Login successful!\n")
        return True
    else:
        print("❌ Invalid credentials. Access denied.\n")
        return False
    