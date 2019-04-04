"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = (temperature_c*1.8) + 32
    return temperature_f
    
def convert_f_to_k(temperature_f):
    """Convert Fahrenheit to Kelvin."""
    temperature_k = (temperature_f-32)*(5/9)+273.15
    return round(temperature_k, 2)

def convert_c_to_k(temperature_c):
    """Convert Celsius to Kelvin."""
    temperature_k = temperature_c + 273.15
    return round(temperature_k, 2)

def convert_k_to_f(temperature_k):
    """Convert Kelvin to Fahrenheit."""
    temperature_f = (9/5)*(temperature_k - 273.15) +32
    return round(temperature_f, 2)

def convert_k_to_c(temperature_k):
    """Convert Kelvin to Celsius."""
    temperature_c = temperature_k - 273.15
    return round(temperature_c, 2)
    