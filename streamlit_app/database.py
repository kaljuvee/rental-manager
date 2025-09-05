import sqlite3
import hashlib
from datetime import datetime
import os

class RentsterDB:
    def __init__(self, db_path="rentster.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Initialize the database with all required tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create Plans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Plans (
                plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                transaction_fee REAL NOT NULL,
                max_users INTEGER NOT NULL,
                max_locations INTEGER NOT NULL
            )
        ''')
        
        # Create Companies table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Companies (
                company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                reg_code TEXT,
                phone TEXT,
                address TEXT,
                website TEXT,
                plan_id INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (plan_id) REFERENCES Plans(plan_id)
            )
        ''')
        
        # Create Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'business_owner', 'customer')),
                company_id INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES Companies(company_id)
            )
        ''')
        
        # Create Locations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Locations (
                location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                company_id INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES Companies(company_id)
            )
        ''')
        
        # Create RentalItems table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS RentalItems (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT,
                company_id INTEGER,
                location_id INTEGER,
                availability_status TEXT NOT NULL CHECK(availability_status IN ('available', 'rented', 'maintenance')),
                rental_price_per_day REAL NOT NULL,
                image_url TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES Companies(company_id),
                FOREIGN KEY (location_id) REFERENCES Locations(location_id)
            )
        ''')
        
        # Create Bookings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER,
                user_id INTEGER,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                total_price REAL NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('confirmed', 'pending', 'completed', 'cancelled')),
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (item_id) REFERENCES RentalItems(item_id),
                FOREIGN KEY (user_id) REFERENCES Users(user_id)
            )
        ''')
        
        # Create Payments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER,
                amount REAL NOT NULL,
                payment_date TEXT NOT NULL,
                payment_method TEXT,
                transaction_id TEXT,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
            )
        ''')
        
        # Create DigitalSignatures table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DigitalSignatures (
                signature_id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER,
                document_id TEXT,
                signature_data TEXT,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
            )
        ''')
        
        # Create AccessControl table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS AccessControl (
                access_id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER,
                user_id INTEGER,
                access_code TEXT,
                valid_from TEXT NOT NULL,
                valid_to TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (location_id) REFERENCES Locations(location_id),
                FOREIGN KEY (user_id) REFERENCES Users(user_id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
        # Insert default plans if they don't exist
        self.insert_default_plans()
    
    def insert_default_plans(self):
        """Insert default subscription plans"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        plans = [
            ("Free", 0.0, 9.0, 1, 1),
            ("Business", 59.0, 0.0, 10, 5),
            ("Premium", 99.0, 0.0, 100, 50)
        ]
        
        for plan in plans:
            cursor.execute('''
                INSERT OR IGNORE INTO Plans (name, price, transaction_fee, max_users, max_locations)
                VALUES (?, ?, ?, ?, ?)
            ''', plan)
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hash a password for storing"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, username, email, password, role='customer', company_id=None):
        """Create a new user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        password_hash = self.hash_password(password)
        
        try:
            cursor.execute('''
                INSERT INTO Users (username, email, password_hash, role, company_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, email, password_hash, role, company_id))
            
            user_id = cursor.lastrowid
            conn.commit()
            return user_id
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
    
    def authenticate_user(self, email, password):
        """Authenticate a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        password_hash = self.hash_password(password)
        
        cursor.execute('''
            SELECT user_id, username, email, role, company_id
            FROM Users
            WHERE email = ? AND password_hash = ?
        ''', (email, password_hash))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return {
                'user_id': user[0],
                'username': user[1],
                'email': user[2],
                'role': user[3],
                'company_id': user[4]
            }
        return None
    
    def get_rental_items(self, company_id=None):
        """Get all rental items, optionally filtered by company"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if company_id:
            cursor.execute('''
                SELECT ri.*, c.name as company_name, l.name as location_name
                FROM RentalItems ri
                LEFT JOIN Companies c ON ri.company_id = c.company_id
                LEFT JOIN Locations l ON ri.location_id = l.location_id
                WHERE ri.company_id = ?
            ''', (company_id,))
        else:
            cursor.execute('''
                SELECT ri.*, c.name as company_name, l.name as location_name
                FROM RentalItems ri
                LEFT JOIN Companies c ON ri.company_id = c.company_id
                LEFT JOIN Locations l ON ri.location_id = l.location_id
            ''')
        
        items = cursor.fetchall()
        conn.close()
        return items
    
    def create_booking(self, item_id, user_id, start_date, end_date, total_price):
        """Create a new booking"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Bookings (item_id, user_id, start_date, end_date, total_price, status)
            VALUES (?, ?, ?, ?, ?, 'pending')
        ''', (item_id, user_id, start_date, end_date, total_price))
        
        booking_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return booking_id
    
    def get_bookings(self, user_id=None, company_id=None):
        """Get bookings, optionally filtered by user or company"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if user_id:
            cursor.execute('''
                SELECT b.*, ri.name as item_name, u.username
                FROM Bookings b
                JOIN RentalItems ri ON b.item_id = ri.item_id
                JOIN Users u ON b.user_id = u.user_id
                WHERE b.user_id = ?
                ORDER BY b.created_at DESC
            ''', (user_id,))
        elif company_id:
            cursor.execute('''
                SELECT b.*, ri.name as item_name, u.username
                FROM Bookings b
                JOIN RentalItems ri ON b.item_id = ri.item_id
                JOIN Users u ON b.user_id = u.user_id
                WHERE ri.company_id = ?
                ORDER BY b.created_at DESC
            ''', (company_id,))
        else:
            cursor.execute('''
                SELECT b.*, ri.name as item_name, u.username
                FROM Bookings b
                JOIN RentalItems ri ON b.item_id = ri.item_id
                JOIN Users u ON b.user_id = u.user_id
                ORDER BY b.created_at DESC
            ''')
        
        bookings = cursor.fetchall()
        conn.close()
        return bookings

