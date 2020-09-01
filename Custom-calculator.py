#Calculates the max horsepower output of an engine based on max engine speed and torque

#initializing variables
horse_power = 0 
engine_speed = 0
engine_torque = 0
CONSTANT = 5252

#getting user input for engine speed and torque
print("\nFind out the max horsepower output of an engine.")
engine_speed = int(input("What is the max engine speed in RPMs?:\n"))
engine_torque = int(input("What is the max engine torque in lb/ft?:\n"))

#performing calculation
horse_power = int((engine_speed * engine_torque)/CONSTANT)

#print result
print(f"This engine's max horsepower output about {horse_power} HP @ {engine_speed} RPMs with {engine_torque} lbs of torque\n")

