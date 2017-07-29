"""A simple module for defining Cars"""

class Car:
    """Our Car class"""

    def __init__(self,
                 year: int,
                 make: str,
                 model: str,
                 top_speed: float,
                 acceleration: float
                ):
        """Car Constructor function"""
        self.year = year
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.current_speed = 0
        self.odometer = 0

    def __str__(self):
        return str(self.year) + " " + self.make + " " + self.model

    def advance(self):
        """
        Speed up the car...if possible
        Also, we need to increment the odometer
        """
        if self.current_speed < self.top_speed:
            self.current_speed += self.acceleration

            if self.current_speed > self.top_speed:
                self.current_speed = self.top_speed

        self.odometer += (self.current_speed / 60 ) / 60

