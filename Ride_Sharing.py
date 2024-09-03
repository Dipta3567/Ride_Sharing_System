class Ride_Sharing:
    def __init__(self,name) -> None:
        self.id=1234567890
        self.name=name
        self.riders=[]
        self.customers=[]
        self.admins=[]
        self.income=0
        self.income_history=[]
        self.pending_request=[]
        self.running_request=[]
        self.completed_request=[]
        self.canceled_request=[]
        



    def add_rider(self,rider):
        if not self.riders:
            self.riders.append(rider)
            print("Account Created Successfully\n")
            return True
        for emp in self.riders:
            if (emp.nid==rider.nid):
                print("This rider already exist\n")
                return False
        self.riders.append(rider)
        print("Account Created Successfully\n")
        return True
    



    def add_customer(self,customer):
        if not self.customers:
            self.customers.append(customer)
            print("Account Created Successfully\n")
            return True
        for cus in self.customers:
            if (cus.nid==customer.nid):
                print("This customer already exist\n")
                return False
        self.customers.append(customer)
        print("Account Created Successfully\n")
        return True

    def add_admin(self,admin):
        if not self.admins:
            self.admins.append(admin)
            print("Account Created Successfully\n")
            return True
        for adm in self.admins:
            if (adm.nid==admin.nid):
                print("This admin already exist\n")
                return False
        self.admins.append(admin)
        print("Account Created Successfully\n")
        return True

    def login_admin(self,email,password):
        if not self.admins:
            print("There are no admins\n")
            return None
        for adm in self.admins:
            if (adm.email==email and adm.password==password):
                return adm
        return None
    
    def login_rider(self,email,password):
        if not self.riders:
            print("There are no riders\n")
            return None
        for emp in self.riders:
            if (emp.email==email and emp.password==password):
                return emp
        return None
    
    def login_customer(self,email,password):
        if not self.customers:
            print("There are no customers\n")
            return None
        for cus in self.customers:
            if (cus.email==email and cus.password==password):
                return cus
        return None

    def view_riders(self):
        if not self.riders:
            print("There are no riders\n")
            return
        opt=int(input("1. All Rider List\n2. Car Rider List\n3. Bike Rider List\n4. Cng Rider List\nOption: "))
        if (opt==1):
            print("*****************Rider List****************\n")
            print("ID\t\tName\t\tEmail\t\tPhone\t\tNID\t\tAddress\t\tVehicle_Type\t\tLicenence")
            for emp in self.riders:
                print(f"{emp.rider_id}\t\t{emp.name}\t\t{emp.email}\t\t{emp.phone}\t\t{emp.nid}\t\t{emp.address}\t\t{emp.vehicle}\t\t{emp.licence}")

        elif (opt==2):
            print("*****************Car Riders List****************\n")
            print("ID\t\tName\t\tEmail\t\tPhone\t\tNID\t\tAddress\t\tVehicle_Type\t\tLicenence")
            for emp in self.riders:
                if (emp.vehicle=="car"):
                    print(f"{emp.rider_id}\t\t{emp.name}\t\t{emp.email}\t\t{emp.phone}\t\t{emp.nid}\t\t{emp.address}\t\t{emp.vehicle}\t\t{emp.licence}")

        elif (opt==3):
            print("*****************Bike Riders List****************\n")
            print("ID\t\tName\t\tEmail\t\tPhone\t\tNID\t\tAddress\t\tVehicle_Type\t\tLicenence")
            for emp in self.riders:
                if (emp.vehicle=="bike"):
                    print(f"{emp.rider_id}\t\t{emp.name}\t\t{emp.email}\t\t{emp.phone}\t\t{emp.nid}\t\t{emp.address}\t\t{emp.vehicle}\t\t{emp.licence}")

        elif (opt==4):
            print("*****************Cng Riders List****************\n")
            print("ID\t\tName\t\tEmail\t\tPhone\t\tNID\t\tAddress\t\tVehicle_Type\t\tLicenence")
            for emp in self.riders:
                if (emp.vehicle=="cng"):
                    print(f"{emp.rider_id}\t\t{emp.name}\t\t{emp.email}\t\t{emp.phone}\t\t{emp.nid}\t\t{emp.address}\t\t{emp.vehicle}\t\t{emp.licence}")

    
    def view_customers(self):
        if not self.customers:
            print("There are no customers\n")
            return
        print("*****************All customers List****************\n")
        print("ID\t\tName\t\tEmail\t\tPhone\t\tNID\t\tAddress")
        for emp in self.customers:
            print(f"{emp.user_id}\t\t{emp.name}\t\t{emp.email}\t\t{emp.phone}\t\t{emp.nid}\t\t{emp.address}")

    
    def view_income_history(self):
        if not self.income_history:
            print("There are no income history!!!\n")
            return
        print("\n\n******************Income History************************")
        print(f"{self.name} account\t\tAmount\t\tPaid By\t\tDate")
        for his in self.income_history:
            print(f"{his.transfer}\t\t\t{his.amount}\t\t{his.account}\t\t{his.date}\n")
        print(f"\n\nTotal Income: {self.income}\n\n")
    

    def total_income(self):
        print(f"\n\nTotal Income: {self.income}\n\n")
    

    def ride_request(self,request):
        self.pending_request.append(request)
    
    def accecpted_request(self,request):
        self.running_request.append(request)

    def finished_request(self,request):
        self.completed_request.append(request)

            
    def find_rider(self,id):
        if not self.riders:
            print("There are no riders\n")
            return None
        for rider in self.riders:
            if (rider.rider_id==id):
                return rider
        return None
    
    def find_user(self,id):
        if not self.customers:
            print("There are no customers\n")
            return None
        for user in self.customers:
            if (user.user_id==id):
                return user
        return None
    
    def find_pending_req(self,id):
        if not self.pending_request:
            print("There are no request")
            return None
        for req in self.pending_request:
            if (req.request_id==id):
                return req
        return None
    
    def find_accecpted_req(self,id):
        if not self.running_request:
            print("There are no request")
            return None
        for req in self.running_request:
            if (req.request_id==id):
                return req
        return None
    
    def find_completed_req(self,id):
        if not self.completed_request:
            print("There are no request")
            return None
        for req in self.completed_request:
            if (req.request_id==id):
                return req
        return None
    

    def find_canceled_req(self,id):
        if not self.canceled_request:
            print("There are no request")
            return None
        for req in self.canceled_request:
            if (req.request_id==id):
                return req
        return None
    

    def rider_data(self,id):
        if not self.riders:
            print("There are no riders\n")
            return
        rider=self.find_rider(id)
        if rider:
            print("*************************Rider data************************\n")
            print("Rider_ID\t\t\tName\t\t\tPhone\t\t\tEmail\t\t\tAddress\t\t\tNID\t\t\tVehicle\t\t\tLicence")
            print(f"{rider.rider_id}\t\t\t{rider.name}\t\t\t{rider.phone}\t\t\t{rider.email}\t\t\t{rider.address}\t\t\t{rider.nid}\t\t\t{rider.vehicle}\t\t\t{rider.licence}\n\n")
        else:
            print(f"There are no rider with  this ID : {id}\n")
            return
    
    def user_data(self,id):
        if not self.customers:
            print("There are no customers\n")
            return
        user=self.find_user(id)
        if user:
            print("*************************Customer data************************\n")
            print("User_ID\t\t\tName\t\t\tPhone\t\t\tEmail\t\t\tNID")
            print(f"{user.user_id}\t\t\t{user.name}\t\t\t{user.phone}\t\t\t{user.email}\t\t\t{user.nid}\n\n")
        else:
            print(f"There are no user with  this ID : {id}\n")
            return

    def check_all_pending_request(self):
        if not self.pending_request:
            print("There are no pending request\n")
            return
        print("*****************All Pending Request List****************\n")
        print("Request_ID\t\t\tUser_ID\t\t\tFrom\t\t\tTo\t\t\tDate&Time\n\n") 
        for req in self.pending_request:
            print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\n")
        print("\n\n")

    def check_all_running_request(self):
        if not self.accecpted_request:
            print("There are no running request\n")
            return
        print("*****************All Running Request List****************\n")
        print("Request_ID\t\t\tUser_ID\t\t\tRider_ID\t\t\tFrom\t\t\tTo\t\t\tDate&Time\n\n")
        for req in self.running_request:
            print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.rider}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\n")
        print("\n\n")

    def check_all_completed_request(self):
        if not self.completed_request:
            print("There are no completed request\n")
            return
        print("*****************All Completed Request List****************\n")
        print("Request_ID\t\t\tUser_ID\t\t\tRider_ID\t\t\tFrom\t\t\tTo\t\t\tRequest_Date&Time\t\t\tCompleted_Date&Time\t\t\tFare\t\t\tStatus\n\n")
        for req in self.completed_request:
            print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.rider}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\t\t\t{req.completed_time}\t\t\t{req.fare_price}\t\t\t{req.paid}\n")
        print("\n\n")

    def check_all_canceled_request(self):
        if not self.canceled_request:
            print("There are no canceled request\n")
            return
        print("*****************All Canceled Request List****************\n")
        print("Request_ID\t\t\tUser_ID\t\t\tFrom\t\t\tTo\t\t\tRequest_Date&Time\t\t\tCancel_Date&Time\t\t\tFine\t\t\tStatus\n\n")
        for req in self.canceled_request:
            print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\t\t\t{req.cancel_time}\t\t\t{req.fine}\t\t\t{req.fine_paid}\n")
        print("\n\n")

    def check_req(self,req_id):
        req=self.find_pending_req(req_id)
        if req:
            print("*****************Request Details****************\n")
            print("Request_ID\t\t\tUser_ID\t\t\tFrom\t\t\tTo\t\t\tDate&Time\n\n")
            print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\n")
        else:
            req=self.find_accecpted_req(req_id)
            if req:
                print("*****************Request Details****************\n")
                print("Request_ID\t\t\tUser_ID\t\t\tRider_ID\t\t\tFrom\t\t\tTo\t\t\tDate&Time\n\n")
                print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.rider}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\n")
            else:
                req=self.find_completed_req(req_id)
                if req:
                    print("*****************Request Details****************\n")
                    print("Request_ID\t\t\tUser_ID\t\t\tRider_ID\t\t\tFrom\t\t\tTo\t\t\tRequest_Date&Time\t\t\tCompleted_Date&Time\t\t\tFare\t\t\tStatus\n\n")
                    print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.rider}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\t\t\t{req.completed_time}\t\t\t{req.fare_price}\t\t\t{req.paid}\n")
                else:
                    req=self.find_canceled_req(req_id)
                    if req:
                        print("*****************Request Details****************\n")
                        print("Request_ID\t\t\tUser_ID\t\t\tFrom\t\t\tTo\t\t\tRequest_Date&Time\t\t\tCancel_Date&Time\t\t\tFine\t\t\tStatus\n\n")
                        print(f"{req.request_id}\t\t\t{req.customer}\t\t\t{req.cus_current}\t\t\t{req.cus_des}\t\t\t{req.request_time}\t\t\t{req.cancel_time}\t\t\t{req.fine}\t\t\t{req.fine_paid}\n")
                    else:
                        print(f"There are no request with this ID : {req_id}\n")
                        return

