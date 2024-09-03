import time
from users import User,Admin,Rider,Customer
from Ride_Sharing import Ride_Sharing
from Ride import Ride
from Transaction import Transaction
from datetime import datetime
import os

uber=Ride_Sharing("Uber")



def admin_system(admin):
    while True:
        print(f"********************************Welcome to Admin Panel  of {uber.name}********************************\n\n")
        print(f"Welcome {admin.name}\n\n")
        op=int(input("1. view all riders\n2. View all customers\n3. View income history\n4. View total income\n5. Check Rider Data\n6. Check Customer Data\n7. Check All Pending Request\n8. Check All Running Request\n9. Check All Completed Request\n10. Check All Cancelled Request\n11. Check Ride Request Data\n12. Exit\nEnter Your Choice : "))
        if op==1:
            admin.view_all_riders(uber)

        elif op==2:
            admin.view_all_customers(uber)

        elif op==3:
            admin.income_history(uber)

        elif op==4:
            admin.total_income(uber)

        elif op==5:
            id=input("Enter Rider ID : ")
            admin.check_rider_data(uber,id)

        elif op==6:
            id=input("Enter Customer ID : ")
            admin.check_user_data(uber,id)

        elif op==7:
            admin.check_all_pending_request(uber)

        elif op==8:
            admin.check_all_running_request(uber)

        elif op==9:
            admin.check_all_completed_request(uber)

        elif op==10:
            admin.check_all_cancelled_request(uber)

        elif op==11:
            id=input("Enter Ride Request ID : ")
            admin.check_request_info(uber,id)

        else:
            break


    

def admin_interface():
    print("1. Create New Account\n2. Login in Existing Account\n3. Exit")
    c=int(input("Enter Your Choice : "))
    if c==1:
        name=input("Enter Your Name : ")
        email=input("Enter Your Email : ")
        phone=input("Enter Your Phone : ")
        nid=input("Enter Your NID : ")
        while True:
            password=input("Create new password : ")
            repas=input("Re-Enter Password : ")
            if password==repas:
                break
        admin=Admin(name=name,email=email,phone=phone,nid=nid,password=password)
        status=uber.add_admin(admin)
        if status:
            time.sleep(1)
            os.system('cls')
            admin_system(admin)
        else:
            return
    
    elif c==2:
        email=input("Enter Your Email : ")
        password=input("Enter Your Password : ")
        admin=uber.login_admin(email,password)
        if admin:
            time.sleep(1)
            os.system('cls')
            admin_system(admin)
        else:
            print("Invalid Email or Password")
            return
    else:
        return
    




def rider_system(rider):
    while True:
        print(f"********************************Welcome to Rider Panel  of {uber.name}********************************\n\n")
        print(f"Welcome {rider.name}\n\n")
        op=int(input("1. Search Customer\n2. Accecpt Request\n3. Complete Request\n4. Cancel Request\n5. Top-up wallet\n6. Pay charge\n7. Withdraw balance\n8. Transaction Hisory\n9. Travel History\n10. Exit\nEnter Your Choice : "))

        if op==1:
            rider.search_customer(uber)

        elif op==2:
            id=input("Enter Request ID : ")
            rider.accecpt_request(uber,id)

        elif op==3:
            rider.completed_request(uber)

        elif op==4:
            rider.cancel_request(uber)

        elif op==5:
            amount=int(input("Enter the amount you want to top-up in your account : "))
            rider.top_up(amount)

        elif op==6:
            rider.pay_charge(uber)

        elif op==7:
            amount=int(input("Enter the amount you want to withdraw from your account : "))
            rider.withdraw(amount)

        elif op==8:
            rider.transaction_history()

        elif op==9:
            rider.travel_history()

        else:
            break
    


def rider_interface():
    print("1. Create New Account\n2. Login in Existing Account\n3. Exit")
    c=int(input("Enter Your Choice : "))
    if c==1:
        name=input("Enter Your Name : ")
        email=input("Enter Your Email : ")
        phone=input("Enter Your Phone : ")
        nid=input("Enter Your NID : ")
        address=input("Enter Your Address : ")
        while True:
            op=int(input("Enter Your Vehicle Type : \n1. Car\n2. Bike\n3. Cng\n Choose : "))
            if op==1:
                vehicle="car"
                break
            elif op==2:
                vehicle="bike"
                break
            elif op==3:
                vehicle="cng"
                break
            else:
                print("\n")
                
        while True:
            password=input("Create new password : ")
            repas=input("Re-Enter Password : ")
            if password==repas:
                break
        rider=Rider(name=name,email=email,nid=nid,phone=phone,password=password,address=address,vehicle=vehicle)
        status=uber.add_rider(rider)
        if status:
            time.sleep(1)
            os.system('cls')
            rider_system(rider)
        else:
            return
    
    elif c==2:
        email=input("Enter Your Email : ")
        password=input("Enter Your Password : ")
        rider=uber.login_rider(email,password)
        if rider:
            time.sleep(1)
            os.system('cls')
            rider_system(rider)
        else:
            print("Invalid Email or Password")
            return
    else:
        return
    


def customer_system(user):
    while True:
        print(f"********************************Welcome to User Panel  of {uber.name}********************************\n\n")
        print(f"Welcome {user.name}\n\n")
        op=int(input("1. Top-up account\n2. Request Ride\n3. Cancel Ride Request\n4. Pay Bill\n5. Transaction History\n6. Travel History\n7. Exit\nEnter Your Choice : "))
        if op==1:
            amount=int(input("Enter the amount you want to top-up in your account : "))
            user.recharge(amount)

        elif op==2:
            user.request_ride(uber)

        elif op==3:
            user.cancel_ride_req(uber)

        elif op==4:
            user.pay_bill(uber)

        elif op==5:
            user.transaction_history()

        elif op==6:
            user.travel_history()

        else:
            break
    

    
def customer_interface():
    print("1. Create New Account\n2. Login in Existing Account\n3. Exit")
    c=int(input("Enter Your Choice : "))
    if c==1:
        name=input("Enter Your Name : ")
        email=input("Enter Your Email : ")
        phone=input("Enter Your Phone : ")
        nid=input("Enter Your NID : ")      
        while True:
            password=input("Create new password : ")
            repas=input("Re-Enter Password : ")
            if password==repas:
                break
        user=Customer(name=name,email=email,nid=nid,phone=phone,password=password)
        status=uber.add_customer(user)
        if status:
            time.sleep(1)
            os.system('cls')
            customer_system(user)
        else:
            return
    
    elif c==2:
        email=input("Enter Your Email : ")
        password=input("Enter Your Password : ")
        user=uber.login_customer(email,password)
        if user:
            time.sleep(1)
            os.system('cls')
            customer_system(user)
        else:
            print("Invalid Email or Password")
            return
    else:
        return
    
# Create riders with different vehicles
rider1 = Rider(name="Rider1", email="rider1", phone="987654321", nid="R1", password="rider123", address="Address1", vehicle="car")
rider2 = Rider(name="Rider2", email="rider2", phone="987654322", nid="R2", password="rider123", address="Address2", vehicle="bike")
rider3 = Rider(name="Rider3", email="rider3", phone="987654323", nid="R3", password="rider123", address="Address3", vehicle="cng")
rider4 = Rider(name="Rider4", email="rider1", phone="987654321", nid="R4", password="rider123", address="Address1", vehicle="car")
rider5 = Rider(name="Rider5", email="rider1", phone="987654321", nid="R5", password="rider123", address="Address1", vehicle="car")
rider6 = Rider(name="Rider6", email="rider6", phone="987654322", nid="R6", password="rider123", address="Address2", vehicle="bike")
uber.add_rider(rider1)
uber.add_rider(rider2)
uber.add_rider(rider3)
uber.add_rider(rider4)
uber.add_rider(rider5)
uber.add_rider(rider6)

os.system('cls')

while True:
    print(f"********Welcome To {uber.name} Ride Sharing Service******")
    print("1. Admin Panel")
    print("2. Rider Panel")
    print("3. Customer Panel")
    print("4.Exit")
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        os.system('cls')
        admin_interface()
    elif choice==2:
        os.system('cls')
        rider_interface()
    elif choice==3:
        os.system('cls')
        customer_interface()
    elif choice==4:
        break
    else:
        print("Invalid")





