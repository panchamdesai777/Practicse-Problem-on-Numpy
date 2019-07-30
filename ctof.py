#Convert from Centigrade to Fahrenheit
# Code starts here
import numpy as np

# centigrade temperatures
centigrade_temps = np.array([0, 10, 25, 32, 80, 99.99])

# function for conversion
def convert(celsius):
    return (celsius* 9/5) + 32
fahrenheit_temps = convert(centigrade_temps)
print(fahrenheit_temps)

