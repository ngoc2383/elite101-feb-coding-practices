def scale_from():
    scale = None
    while scale is None: # Repeart the loop until the user enters a valid scale
        scale = input("Which scale are you converting from? (C/F/K): ")
        if scale != "C" and scale != "F" and scale != "K": # if the scale is not C, F, or K; it is invalid --> repeat the loop
            print("Invalid scale.")
            scale = None
    return scale

def scale_to(): 
    scale = None
    while scale is None:
        scale = input("Which scale are you converting to? (C/F/K): ")
        if scale != "C" and scale != "F" and scale != "K":
            print("Invalid scale.")
            scale = None
    return scale

def temperature_converter(): # Take the scales provided by the user and convert to the desired scale
    scale_from = scale_from()
    scale_to = scale_to()
    temperature = float(input(f"Enter the temperature in {scale_from}: ")) # Make sure the temperature is a float
    if scale_from == "C" and scale_to == "F": # Different formulas for different conversions
        result = (temperature * 9/5) + 32
    elif scale_from == "C" and scale_to == "K":
        result = temperature + 273.15
    elif scale_from == "F" and scale_to == "C":
        result = (temperature - 32) * 5/9
    elif scale_from == "F" and scale_to == "K":
        result = (temperature - 32) * 5/9 + 273.15
    elif scale_from == "K" and scale_to == "C":
        result = temperature - 273.15
    elif scale_from == "K" and scale_to == "F":
        result = (temperature - 273.15) * 9/5 + 32
    else:
        result = temperature
    print(f"The temperature is {result} {scale_to}") # Print the result
        