#!/usr/bin/env pybricks-micropython 


# This line tells the EV3 brick that this file should run using
# the Pybricks MicroPython environment.

# Import the EV3 brick object so we can control the brick itself
# (speaker, screen, buttons, etc.)
from pybricks.hubs import EV3Brick

# Import the Motor class so we can control motors connected to the EV3
from pybricks.ev3devices import Motor

# Import helpful constants:
# Port = which port the motor is plugged into
# Stop = how the motor should stop
# Direction = motor rotation direction (not used here yet)
from pybricks.parameters import Port, Stop, Direction

# Import wait() so we can pause the program if needed
from pybricks.tools import wait


# ----------------------------
# CREATE OBJECTS
# ----------------------------

# Create an object representing the EV3 brick itself.
# This lets us control things like the speaker or screen.
ev3 = EV3Brick()

# Create a motor object.
# This tells Python there is a motor plugged into Port A.
motor_b = Motor(Port.A)


# ----------------------------
# MAIN PROGRAM
# ----------------------------

# Make the EV3 brick play a short beep sound.
# This is often used to signal the start of a program.
ev3.speaker.beep()

# Print a message to the EV3 console so we know what the robot is doing.
print("Moving motor forward...")

# Run the motor for a specific amount of time.
# speed = how fast the motor spins
# time = how long it runs (milliseconds)
# 2000 ms = 2 seconds
motor_b.run_time(speed=-500, time=2000)

# Run the motor until it reaches a specific angle.
# speed = how fast it moves
# target_angle = how many degrees to rotate
# 360 degrees = one full rotationu
# Stop.HOLD = motor resists movement when finished
motor_b.run_target(speed=650, target_angle=-36000, then=Stop.HOLD)

# Print a final message so we know the program finished.
print("Done!")  # test message