from users import Admin, Rider, Customer
from Ride_Sharing import Ride_Sharing
from Ride import Ride
from Transaction import Transaction
from datetime import datetime
import os

# Create an instance of the Ride Sharing System
uber = Ride_Sharing("Uber")

# Create admin
admin1 = Admin(name="Admin1", email="admin1", phone="123456789", nid="A1", password="admin123")
uber.add_admin(admin1)

# Create riders with different vehicles
rider1 = Rider(name="Rider1", email="rider1", phone="987654321", nid="R1", password="rider123", address="Address1", vehicle="car")
rider2 = Rider(name="Rider2", email="rider2", phone="987654322", nid="R2", password="rider123", address="Address2", vehicle="bike")
rider3 = Rider(name="Rider3", email="rider3", phone="987654323", nid="R3", password="rider123", address="Address3", vehicle="cng")
rider1 = Rider(name="Rider4", email="rider1", phone="987654321", nid="R4", password="rider123", address="Address1", vehicle="car")
rider1 = Rider(name="Rider5", email="rider1", phone="987654321", nid="R5", password="rider123", address="Address1", vehicle="car")
rider2 = Rider(name="Rider6", email="rider6", phone="987654322", nid="R6", password="rider123", address="Address2", vehicle="bike")
uber.add_rider(rider1)
uber.add_rider(rider2)
uber.add_rider(rider3)

