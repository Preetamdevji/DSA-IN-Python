from abc import ABC, abstractmethod


class Ride(ABC):
    def __init__(self,origin,destination,fare,driver,passenger):
        self.origin = origin
        self.destination = destination
        self.fare = fare
        self.driver = driver
        self.passenger = passenger
        

    def calculate_fare(self):
        rate_per_km = 10
        distance = self.origin - self.destination
        self.fare = rate_per_km * distance 


    def start_ride(self):
        print(f"Ride started from {self.origin} to {self.destination}.")
        self.driver = False
        

    def end_ride(self):
        print("Ride ended")
        self.driver = True

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def generate_invoice(self):
        pass


class Passenger():
    def __init__(self, name, phone, wallet_balance):
        self.name = name
        self.__phone = phone
        self._wallet_balance = wallet_balance    
        pass


    def request_ride(self,  ride_type, origin, destination, driver):
        if ride_type == "poll":
            ride = PoolRide(origin,destination, 0, driver, self, shared_with_count=1 )
        else:
            ride = PremiumRide(origin, destination, 0, driver, luxury_level="High")

        ride.calculate_fare()
        ride.start_ride()
        ride.end_ride()
        ride.make_payment()
        ride.generate_invoice()
    

    def add_money(self, amount):
        if amount > 0:
            self._wallet_balance += amount
            print(f"Rs: {amount} added to walled. New balance is Rs: {self._wallet_balance}")
        else:
            print(f"Invalid Amount") 


class Driver():
    def __init__(self, name, car_model, rating, is_available=True):
        self.name = name
        self.car_model = car_model
        self._rating = rating
        self.is_available = is_available
        self.current_location = None
        self.current_ride = None
        
    
    def accept_ride(self, ride):
        if self.is_available:
            self.is_available = False
            self.current_ride = ride
            print(f"{self.name} has accepted the ride from {ride.origin} to {ride.destination}.")
        else: 
            print(f"{self.name} is currently not available to take a new ride.")    


    def complete_ride(self):
        if self.current_ride:
            print(f"{self.name} has completed the ride from {self.current_ride.origin} to {self.current_ride.destination}.")
            self.current_ride = None
            self.is_available = True

    def update_location(self, new_location):
        self.current_location = new_location
        print(f"{self.name}'s location updated to {new_location}.")


class PoolRide(Ride):
    def __init__(self, origin, destination, fare, driver, passenger, shared_with_count):
        super().__init__(origin, destination, fare, driver, passenger)
        self.shared_with_count = shared_with_count
        self.passengers = [passenger]  # List to store all passengers (shared)

    def calculate_fare(self):
        # Fare should be divided among all passengers (including main one)
        total_passengers = len(self.passengers)
        if total_passengers > 0:
            individual_fare = self.fare / total_passengers
            print(f"Fare per passenger: ₹{individual_fare}")
            return individual_fare
        else:
            print("No passengers in ride.")
            return 0

    def add_passenger(self, passenger):
        # Pool ride mein new passenger add karo jab tak shared limit na cross ho
        if len(self.passengers) < self.shared_with_count:
            self.passengers.append(passenger)
            print(f"{passenger.name} added to the pool ride.")
        else:
            print("Cannot add more passengers. Pool ride is full.")



class PremiumRide(Ride):
    def __init__(self, origin, destination, fare, driver, passenger, luxury_level):
        super().__init__(origin, destination, fare, driver, passenger)
        self.luxury_level = luxury_level  

    def calculate_fare(self):
        multipliers = {
            'Gold': 1.2,
            'Platinum': 1.5,
            'Diamond': 2.0
        }
        multiplier = multipliers.get(self.luxury_level, 1.0)
        premium_fare = self.fare * multiplier
        print(f"Luxury Level: {self.luxury_level} → Total Premium Fare: ₹{premium_fare}")
        return premium_fare



class PaymentInterface(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass


    @abstractmethod
    def generate_invoice(self):
        pass



class Admin():

    def __init__(self, name, role, password):
        self.name = name
        self.role = role
        self.__password = password
    
    def view_all_rides(self):
        pass

    def block_user(self):
        pass
    
    def generate_report(self):
        pass
