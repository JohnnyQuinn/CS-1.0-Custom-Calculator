horse_power = 0
engine_speed = 0
engine_torque = 0
CONSTANT = 5252

print("Find out the horsepower output of an engine at a certain engine speed:")
engine_speed = int(input("What is the engine speed in RPMs?:\n"))
engine_torque = int(input("What is the engine torque?:\n"))

horse_power = int((engine_speed * engine_torque)/CONSTANT)

print(f"This engine outputs about {horse_power} HP at {engine_speed} RPMs with {engine_torque} lbs of torque")

