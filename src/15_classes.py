# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):  # constructor
        self.lat = lat
        self.lon = lon

    def __str__(self):
        s = f"Lat is {self.lat} and lon is {self.lon}\n"
        return s


ll = LatLon(12, 96)

print("ll: ", ll)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):  # constructor
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        s = f"Name is {self.name}, lat is {self.lat} and lon is {self.lon}\n"
        return s


w = Waypoint("Rory", 22, -96)
print("w: ", w)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):  # constructor
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        s = f"Name is {self.name}, difficulty is {self.difficulty}, size is {self.size} lat is {self.lat} and lon is {self.lon}\n"
        return s


g = Geocache("Rory", 3, 22, -96)
print("g: ", g)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
w1 = Waypoint("Catacombs", 41.70505, -121.51521)
print("w1: ", w1)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# uncomment
# print(waypoint)
# uncomment

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print("g: ", g)

# Print it--also make this print more nicely

# uncomment
# print(geocache)
# uncomment
