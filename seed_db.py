from backend.database import users_collection
from backend.auth import get_password_hash
from datetime import datetime

def create_test_accounts():
    # Admin Account
    if not users_collection.find_one({"email": "admin@test.com"}):
        users_collection.insert_one({
            "email": "admin@test.com",
            "password": get_password_hash("admin123"),
            "role": "admin",
            "created_at": datetime.utcnow()
        })
        print("Created Admin: admin@test.com / admin123")
    
    # Student Account
    if not users_collection.find_one({"email": "student@test.com"}):
        users_collection.insert_one({
            "email": "student@test.com",
            "password": get_password_hash("student123"),
            "role": "user",
            "created_at": datetime.utcnow()
        })
        print("Created Student: student@test.com / student123")

if __name__ == "__main__":
    create_test_accounts()
