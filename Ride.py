import string,random

def generate_distance():
    char = string.digits
    distance = ''.join(random.choice(char) for _ in range(2))
    return int(distance)

def price(type,distance):
    if (type=='car'):
        return int(90*distance)
    elif (type=='bike'):
        return int(50*distance)
    elif (type=='cng'):
        return int(30*distance)
    
def generate_ride_req_id():
    char = string.hexdigits
    req_id = ''.join(random.choice(char) for _ in range(5))
    return "Request_ID_"+req_id


class Ride:
    def __init__(self,customer,cus_current,cus_des,cus_choice,req_time) -> None:
        self.request_id=generate_ride_req_id()
        self.customer=customer
        self.rider=None
        self.cus_current=cus_current
        self.cus_des=cus_des
        self.cus_choice=cus_choice
        self.distance=generate_distance()
        self.fare_price=price(cus_choice,self.distance)
        self.request_time=req_time
        self.req_accecpt=False
        self.req_completed=False
        self.paid=False
        self.fine=0
        self.fine_paid=False
        self.ride_canceled=False
        self.cancel_time=None
        self.completed_time=None




