"""Defining a race between two Cars"""

from Car import Car

class Race:
    """Our Race between two cars"""

    def __init__(self, racers: list, distance: float):
        """Construct the race"""
        self.racers = racers
        self.distance = distance
        self.elapsed_time = 0

    def tick(self) -> Car:
        """
        Advance the race by 1 unit of time
        Return the current leader
        """
        self.elapsed_time += 1
        for car in self.racers:
            car.advance()

        leader: Car = self.racers[0]
        for car in self.racers[1:]:
            if car.odometer > leader.odometer:
                leader = car

        return leader
    
    def run(self) -> Car:
        """Run the race"""

        # Advance time until someone crosses the finish line
        finish_line = False

        while not finish_line:
            leader = self.tick()

            # Check if the leader crossed the line
            if leader.odometer >= self.distance:
                return leader


demon: Car = Car(2017, "Dodge", "Demon", 168.0, 25.22)
tesla: Car = Car(2017, "Tesla", "P100D", 155.0, 26.37)

cars: list = [demon, tesla]

race: Race = Race(cars, .20)

winner: Car = race.run()

print("Winner:" , winner, "\n")

for car in race.racers:
    print(car)
    print(car.odometer)
    print(car.current_speed, "\n")
