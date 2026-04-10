#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the Motors and Sensor
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
touch_sensor = TouchSensor(Port.S1)

# Initialize the DriveBase (adjust wheel_diameter and axle_track for your bot)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Variable to track how many times the button was pressed
press_count = 0

while True:
    # 1. Wait for the sensor to be pressed
    while not touch_sensor.pressed():
        wait(10)
    
    # Increment the count
    press_count += 1
    ev3.speaker.beep() # Audio feedback for the press
    
    # 2. Wait for the sensor to be released before moving to the next step
    # This prevents the program from "skipping" counts
    while touch_sensor.pressed():
        wait(10)

    # 3. Perform action based on the number of presses
    if press_count == 1:
        # Spin in place
        robot.drive(0, 180) 
        
    elif press_count == 2:
        # Drive forward
        robot.drive(-3                                                    00, 0)
        
    elif press_count == 3:
        # Stop and reset the counter
        robot.stop()
        press_count = 0

        # The goal is just to make a robot that does a different action every time you push the button.
        # If the button is pressed it should either turn, move, or stop
        # It continues doing whatever its last function was
        # "Press button
        # 1. Spin in place
        # Press button
        # 2. Drive forward
        # Press button
        # 3. Stop
        # Restart"
