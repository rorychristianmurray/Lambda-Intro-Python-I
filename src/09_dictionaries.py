"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]
# get latitude from the first dictionary in the list
print("get latitude from the first dictionary in the list:",
      waypoints[0]["lat"])

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append({
    "lat": 28,
    "lon": 96,
    "name": "a fourth place"
})
print(waypoints)


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
print("**********************")
print("**********************")
print("**********************")
waypoints[0]['name'] = "not a real place"
waypoints[0]['lon'] = -130
print("edited", waypoints)


# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for i in waypoints:
    print(f"waypoint {i['name']} lat is {i['lat']} and lon is {i['lat']}")

print("**********************")
print("**********************")
print("**********************")

# for i in waypoints:
#     for k, v in waypoints[i].items():
#         print("key:value", k, v)
