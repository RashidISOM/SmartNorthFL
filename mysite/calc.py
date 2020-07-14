#Credit to https://stackoverflow.com/questions/4716017/django-how-can-i-find-the-distance-between-two-locations
from math import sin, cos, radians, acos

# http://en.wikipedia.org/wiki/Earth_radius
# """For Earth, the mean radius is 6,371.009 km (˜3,958.761 mi; ˜3,440.069 nmi)"""
EARTH_RADIUS_IN_MILES = 3958.761

def calc_dist_fixed(lat_a, long_a, lat_b, long_b):
    """all angles in degrees, result in miles"""
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    delta_long = radians(long_a - long_b)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES

# Python program for implementation of Bubble Sort 
# Shamelessly stolen from https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubbleSort(arr):
    n = len(arr) - 1

    # Traverse through all array elements 
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed. 
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j][0] > arr[j+1][0] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

