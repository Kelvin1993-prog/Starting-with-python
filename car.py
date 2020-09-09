#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" A class that can be used to represent a car"""

class Car():
    """Summarizes the information regarding cars"""
    
    def __init__(self, make, model, year):
        """initializes attributes to describe car features"""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
    
    def get_descriptive(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Prints a statement showing the car's mileage"""
        print("This car has " + str(self.odomoter_reading) + " mile's on it")
    
    def update_odometer(self, mileage):
        """
        Updates the current value of odometer reading.
        Set the odometer reading to a given value and reject 
        change if attempts are made to roll odometer back
        """
        if mileage >= self.odomoter_reading:
            self.odomoter_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        Add a given amount to the odometer readings
        """
        self.odomoter_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=70):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kwh battery")
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)
    
    def upgrade_battery(self):
        """Check the battery size and set the capacity to 85"""
        if self.battery_size != 85:
            self.battery_size = 85
            range = 270
class ElectricCar(Car):
    """Represent aspects of a car, specific to the electric vehicles"""
    
    def __init__(self, make, model, year):
        """
        initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
