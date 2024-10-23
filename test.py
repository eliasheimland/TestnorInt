import pandas as pd

def calculate_final_speed(initial_speed, inclinations):

    final_speed = initial_speed
    
    for added_speed in inclinations: 
        final_speed = final_speed + added_speed

        if final_speed <= 0:
            final_speed = 0

            return final_speed

    return final_speed

print(calculate_final_speed(60, [0, 30, 0, -45, 0]))