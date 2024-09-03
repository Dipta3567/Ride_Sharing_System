from datetime import datetime
from abc import ABC
import random
import string
import time
from Ride import Ride
from Transaction import Transaction

class User(ABC):
    def __init__(self,name,email,nid,phone,password) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        self.phone=phone
        self.password=password


def generate_rider_id():
    char = string.hexdigits
    rider_id = ''.join(random.choice(char) for _ in range(5))
    return "Rider_"+rider_id

def generate_customer_id():
    char = string.hexdigits
    customer_id = ''.join(random.choice(char) for _ in range(5))
    return "user_"+customer_id

def generate_licence(type):
    char = string.hexdigits
    license = ''.join(random.choice(char) for _ in range(3))
    return type+'_'+license

    
    
class Rider(User):
    def __init__(self, name, email, nid, phone, password,address,vehicle) -> None:
        super().__init__(name, email, nid, phone, password)
        self.address=address
        self.travel=[]
        self.income_transaction=[]
        self.pay_transaction=[]
        self.add_amount=[] 
        self.withdraw_amount=[]
        self.rider_id=generate_rider_id()
        self.wallet=0
        self.current_wallet=0
        self.ride=0
        self.vehicle=vehicle
        self.licence=generate_licence(vehicle)
        self.total_ride=0
        self.occupied=False
        self.customer_id=None
        self.ride_req=None
        self.location=None
        
        

    def add_user(self,user):
        self.customer_id=user
        self.occupied=True
    
    def remove_user(self):
        self.customer_id=None
        self.occupied=False
        self.ride_req=None

    def income(self,amount,account):
        self.wallet+=amount
        self.current_wallet+=amount
        print(f"{amount} has been received\n")
        tran=Transaction(account=self.rider_id,amount=amount,date=datetime.now(),transfer=account)
        self.income_transaction.append(tran)

    def pay_charge(self,uber):
        total=0
        if self.ride >0 and self.ride<=100:
            total=int(self.wallet*(5/100))
        elif self.ride>100:
            total=int(self.wallet*(10/100))

        if self.current_wallet<total:
            print("Balance is insufficient!!!\n")
            print("Want to add balance ?\n1. Yes\n2. No\n")
            op=int(input("Choice : "))
            if op==1:
                print(f"You need to add {total-self.current_wallet} Taka")
                tk=int(input("Enter amount you want to add : "))
                tran=Transaction(account=self.rider_id,amount=tk,date=datetime.now(),transfer=0)
                self.add_amount.append(tran)
                if tk==(total-self.current_wallet):
                    self.current_wallet+=tk
                    tran1=Transaction(account=self.rider_id,amount=total,date=datetime.now(),transfer=uber.id)
                    self.pay_transaction.append(tran1)
                    uber.income_history.append(tran1)
                    uber.income+=total
                    self.current_wallet=0
                    self.wallet=0
                    self.ride=0
                    print("Payment Completed")
                elif tk>total:
                    self.current_wallet+=tk
                    if self.current_wallet>total:
                        tran1=Transaction(account=self.rider_id,amount=total,date=datetime.now(),transfer=uber.id)
                        self.pay_transaction.append(tran1)
                        uber.income_history.append(tran1)
                        uber.income+=total
                        self.current_wallet-=total
                        self.wallet=0
                        self.ride=0
                        print("Payment Completed")
                else:
                    self.current_wallet+=tk
                    print(f"{self.name} has to add more {total-self.current_wallet} tk for payment")
                    return
            else:
                return
            
        elif self.current_wallet>=total:
            tran1=Transaction(account=self.rider_id,amount=total,date=datetime.now(),transfer=uber.id)
            self.pay_transaction.append(tran1)
            uber.income_history.append(tran1)
            uber.income+=total
            self.current_wallet-=total
            self.wallet=0
            self.ride=0
            print("Payment Completed")

    def top_up(self,amount):
        self.current_wallet+=amount
        tran=Transaction(account=self.rider_id,amount=amount,date=datetime.now(),transfer=0)
        self.add_amount.append(tran)
    

    def withdraw(self,amount):
        if amount>self.current_wallet:
            print("Insufficient balance!!\n")
            return
        if amount<=0:
            print("Insufficient amount!!\n")
            return
        self.current_wallet-=amount
        tran=Transaction(account=self.rider_id,amount=amount,date=datetime.now(),transfer=0)
        self.withdraw_amount.append(tran)

    
    def search_customer(self,uber):
        if not uber.pending_request:
            print("There are no ride request\n\n")
            return
        print("***************************Ride Request************************\n\n")
        print("Request_ID\t\t\tStart_Loc\t\t\tEnd_Loc\t\t\tPrice")
        for ride in uber.pending_request:
            if ride.cus_choice==self.vehicle:
                print(f"{ride.request_id}\t\t\t{ride.cus_current}\t\t\t{ride.cus_des}\t\t\t{ride.fare_price}\n")
        print("\n\n")

    def accecpt_request(self,uber,id):
        if not uber.pending_request:
            print("There are no ride request\n\n")
            return
        req=uber.find_pending_req(id)
        if req:
            if req.req_accecpt==False:
                user=uber.find_user(req.customer)
                if user:
                    req.req_accecpt=True
                    req.rider=self.rider_id
                    user.add_rider(self.rider_id,uber)
                    self.add_user(user.user_id)
                    uber.pending_request.remove(req)
                    uber.running_request.append(req)
                    self.ride_req=id
                else:
                    print("User Not found\n")
                    uber.pending_request.remove(req)
                    return
            else:
                print("Request has been accecpted by other rider\n")
                return
        else:
            print("Request not found\n")
            return
        
    def completed_request(self,uber):
        if self.ride_req:
            req=uber.find_accecpted_req(self.ride_req)
            if req:
                req.req_completed=True
            else:
                print("Request not found\n")
                self.remove_user()
        else:
            print("Request not found\n")
            return
        
    def cancel_request(self,uber):
        if self.ride_req:
            req=uber.find_accecpted_req(self.ride_req)
            if req:
                if req.rider==self.rider_id:
                    req.req_accecpt=False
                    req.rider=None
                    self.remove_user()
                    self.ride_req=None
                    user=uber.find_user(req.customer)
                    if user:
                        user.remove_rider()
                        uber.pending_request.append(req)
                        uber.running_request.remove(req)
                    else:
                        uber.running_request.remove(req)
                        return
                else:
                    print("You are not the rider of this requested ride\n")
                    self.ride_req=None
                    return
            else:
                print("You did not accecpted any request\n")
                self.ride_req=None
                return
        else:
            print("You did not accecpted any request\n")
            return
    
    def transaction_history(self):
        op=int(input("1. Income Transaction\n2. Payment Transaction\n3. Top-Up Transaction\n4. Withdraw Transaction\nChoose : "))
        if op==1:
            if not self.income_transaction:
                print("You have not done any transaction\n")
                return
            print("*******************Income Transaction History********************\n\n")
            print("Self_Id\t\tAmount\t\t\t\tUser_Account\t\tDate & Time\n\n")
            for tran in self.income_transaction:
                print(f"{tran.account}\t\t{tran.amount}\t\t{tran.transfer}\t\t{tran.date}\n\n")

            print("\n\n")
            return
        elif op==2:
            if not self.pay_transaction:
                print("You have not done any transaction\n")
                return
            print("*******************Payment Transaction History********************\n\n")
            print(f"Self_Id\t\tAmount\t\t\t\tCompany_Account\t\tDate & Time\n\n")
            for tran in self.pay_transaction:
                print(f"{tran.account}\t\t{tran.amount}\t\t{tran.transfer}\t\t{tran.date}\n\n")

            print("\n\n")
            return
        elif op==3:
            if not self.add_amount:
                print("You have not done any transaction\n")
                return
            print("*******************Top-Up Transaction History********************\n\n")
            print(f"Self_Id\t\tAmount\t\tDate & Time\n\n")
            for tran in self.add_amount:
                print(f"{tran.account}\t\t{tran.amount}\t\t{tran.date}\n\n")

            print("\n\n")
            return
        elif op==4:
            if not self.withdraw_amount:
                print("You have not done any transaction\n")
                return
            print("*******************Withdraw Transaction History********************\n\n")
            print(f"Self_Id\t\tAmount\t\tDate & Time\n\n")
            for tran in self.add_amount:
                print(f"{tran.account}\t\t{tran.amount}\t\t{tran.date}\n\n")

            print("\n\n")
            return
        else:
            return
        

    def travel_history(self):
        if not self.travel:
            print("You does not have any travel history with us\n\n")
            return
        print("***************************Travel History*************************\n\n")
        print("From\t\t\tTo\t\t\t\tUser_id\t\t\tCharge")
        for ride in self.travel:
            print(f"{ride.cus_current}\t\t{ride.cus_des}\t\t{ride.customer}\t\t{ride.fare_price}\n\n")


    


class Admin(User):
    def __init__(self, name, email, nid, phone, password) -> None:
        super().__init__(name, email, nid, phone, password)
    
    def view_all_riders(self,uber):
        uber.view_riders()
    
    def view_all_customers(self,uber):
        uber.view_customers()

    def income_history(self,uber):
        uber.view_income_history()
    
    def total_income(self,uber):
        uber.total_income()
    
    def check_rider_data(self,uber,id):
        uber.rider_data(id)
    
    def check_user_data(self,uber,id):
        uber.user_data(id)

    def check_all_pending_request(self,uber):
        uber.check_all_pending_request()
    
    def check_all_running_request(self,uber):
        uber.check_all_running_request()
    
    def check_all_completed_request(self,uber):
        uber.check_all_completed_request()
    
    def check_all_canceled_request(self,uber):
        uber.check_all_canceled_request()

    def check_request_info(self,uber,id):
        uber.check_req(id)
    



class Customer(User):
    def __init__(self, name, email, nid, phone, password) -> None:
        super().__init__(name, email, nid, phone, password)
        self.user_id=generate_customer_id()
        self.balance=0
        self.charge=0
        self.travel=[]
        self.transaction=[]
        self.request_id=None
        self.request_status=False
        self.rider_id=None
        self.current_location=None
        self.destination=None
        
        

    def recharge(self,amount):
        self.balance+=amount

    def add_rider(self,rider_id,uber):
        self.rider_id=rider_id
        self.request_status=True
        time.sleep(1)
        rider=uber.find_rider(rider_id)
        if rider:
            print(f"You have been assigned a rider.\n")
            print("Rider_Name\t\tPhone\t\tRider_Location\t\tLicenence")
            print(f"{rider.name}\t\t{rider.phone}\t\t{rider.location}\t\t{rider.licence}")
        else:
            self.rider_id=None
            self.request_status=False
            return

    def remove_rider(self):
        self.rider_id=None
        self.request_status=False
        time.sleep(1)
        print("Your assigned rider have canceled your ride request")


    def request_ride(self,uber):
        if self.request_id==None:
            self.current_location=input("Enter Your Current Location: ")
            self.destination=input("Enter Your Destination: ")
            while(True):
                x=int(input("Choose vehicle :\n1. Car\n2.Bike\n3.Cng\nOption : "))
                if x==1:
                    choice="car"
                    break
                elif x==2:
                    choice="bike"
                    break
                elif x==3:
                    choice="cng"
                    break
                else:
                    print("Invalid\n")
        
            req=Ride(customer=self.user_id,cus_current=self.current_location,cus_des=self.destination,cus_choice=choice,req_time=datetime.now())
            uber.pending_request.append(req)
            self.request_id=req.request_id
            self.charge=req.fare_price
        else:
            if self.request_status==True:
                req=uber.find_accecpted_req(self.request_id)
                if req:
                    if req.req_completed==True:
                        print("Complete the previous ride payment for requesting for new ride\n")
                        return
                    else:
                        print("Cancel the previous ride and pay the fine for previous accecpted request for new ride\n")
                else:
                    req=uber.find_pending_req(self.request_id)
                    if req:
                        self.request_status=False
                        print("Cancel the previous the ride request for making new ride request\n")
                        return
                    else:
                        self.request_id=None


            else:
                print("Cancel the previous the ride request for making new ride request\n")


        
    def cancel_ride_req(self,uber):
        if self.request_id==None:
            print("There are No ride request")
            return
        print(f"Current requested ride_id : {self.request_id}")
        x=int(input("Do you want to cancel the request : \n1. Yes\n2. No\nChoose: "))
        if x==1:
            if self.request_status==False:
                req=uber.find_pending_req(self.request_id)
                if req:
                    req.cancel_time=datetime.now()
                    req.ride_canceled=True
                    uber.canceled_request.append(req)
                    uber.pending_request.remove(req)
                    self.request_id=None
                    self.destination=None
                    self.current_location=None
                    print("Ride cancellation successfull\n")
                    self.charge=0
                else:
                    self.request_id=None
                    return
                

            else:
                req=uber.find_accecpted_req(self.request_id)
                if req:
                    if req.req_completed==True:
                        print(f"Your ride have been completed. so you cannot cancel the ride. clear the payment of {self.charge}\n")
                        return
                    rider=uber.find_rider(self.rider_id)
                    if rider:
                        fine=req.fare_price*(20/100)
                        print(f"You have to pay fine for this accecpted ride request. Fine amount : {fine}\n Current balance : {self.balance}\n")
                        op=int(input("Want to countinue : \n1. Yes\n2. No\nChoose : "))
                        if op==1:
                            if fine>self.balance:
                                while(True):
                                    bal=int(input(f"You are {fine-self.balance} Tk short in your account.\nEnter the amount to recharge : "))
                                    if bal>=(fine-self.balance):
                                        self.balance+=bal
                                        print("Recharge Successfull\n")
                                        break
                                    else:
                                        self.balance+=bal
                        
                            if self.balance==fine:
                                self.balance=0
                            elif self.balance>fine:
                                self.balance-=fine
                            req.fine=fine
                            req.canceled_request=True
                            req.fine_paid=True
                            req.cancel_time=datetime.now()
                            uber.canceled_request.append(req)
                            uber.running_request.remove(req)
                            self.request_id=None
                            self.destination=None
                            self.request_status=False
                            rider.income(fine,self.user_id)
                            rider.remove_user()
                            self.rider_id=None
                            tran=Transaction(account=self.user_id,amount=fine,date=datetime.now(),transfer=rider.rider_id)
                            self.transaction.append(tran)
                            print("Ride cancellation successfull\n")
                            self.charge=0
                            self.current_location=None
                
                        else:
                            return
                    else:
                        self.rider_id=None
                        self.request_status=False
                        req.rider=None
                        req.req_accecpt=False
                        uber.pending_request.append(req)
                        uber.running_request.remove(req)
                        print("Try again\n")
                        return


                else:
                    self.request_status=False
                    print("Try again\n")
                    return
                    
        else:
            return

    
    def pay_bill(self,uber):
        if self.request_id==None:
            print("You did not request for any ride\n\n")
            return
        if self.request_status==False:
            print("Your ride request have not been accecpted yet\n\n")
            return
        req=uber.find_accecpted_req(self.request_id)
        if req:
            if req.req_completed==True:
                rider=uber.find_rider(self.rider_id)
                if rider:
                    print(f"Confirm payment of {self.charge} for ride : {self.request_id}\n")
                    op=int(input("1. Yes\n2. No\nchoose : "))
                    if op==1:
                        while(True):
                            if self.balance >= req.fare_price:
                                break
                            else:
                                print(f"You are {req.fare_price-self.balance} short in your account\n")
                                tk=int(input("Enter the amount to recharge : "))
                                self.recharge(tk)
                    else:
                        return
                    self.balance-=req.fare_price
                    tran=Transaction(account=self.user_id,amount=self.charge,date=datetime.now(),transfer=rider.rider_id)
                    self.transaction.append(tran)
                    rider.income(self.charge,self.user_id)
                    req.paid=True
                    req.completed_time=datetime.now()
                    self.travel.append(req)
                    rider.travel.append(req)
                    uber.completed_request.append(req)
                    uber.running_request.remove(req)
                    rider.remove_user()
                    self.charge=0
                    self.request_id=None
                    self.request_status=False
                    self.rider_id=None
                    self.current_location=None
                    self.destination=None
                else:
                    req.req_completed=False
                    self.request_status=False
                    self.rider_id=None
                    req.rider=None
                    req.req_accecpt=False
                    req.req_completed=False
                    uber.running_request.remove(req)
                    uber.pending_request.append(req)
            else:
                print("Your ride have not been completed\n")
                return
        else:
            self.request_status=False
        

    def transaction_history(self):
        if not self.transaction:
            print("You have not done any transaction\n")
            return
        print("*******************Transaction History********************\n\n")
        print("Self_Id\t\tAmount\t\t\t\tTransfer_Account\t\tDate & Time\n\n")
        for tran in self.transaction:
            print(f"{tran.account}\t\t{tran.amount}\t\t{tran.transfer}\t\t{tran.date}\n\n")

        print("\n\n")
        return
    
    def travel_history(self):
        if not self.travel:
            print("You does not have any travel history with us\n\n")
            return
        print("***************************Travel History*************************\n\n")
        print("From\t\t\tTo\t\t\t\tRider_id\t\t\tCharge")
        for ride in self.travel:
            print(f"{ride.cus_current}\t\t{ride.cus_des}\t\t{ride.rider}\t\t{ride.fare_price}\n\n")

