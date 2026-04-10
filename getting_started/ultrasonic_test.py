#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import random

ev3 = EV3Brick()
left_motor  = Motor(Port.A)
right_motor = Motor(Port.D)
Drill = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

obstacle_sensor = UltrasonicSensor(Port.S4)

Drill.run(650)

while True:
    distance = obstacle_sensor.distance()

    if distance < 200:
        robot.stop()
        ev3.screen.clear()
        ev3.screen.print("Object detected!")
        ev3.screen.print("Dist: " + str(distance) + " mm")
        
        robot.drive(150, 0)
        wait(500)
        random_angle = random.randint(-180, 180)
        ev3.speaker.beep()

        robot.turn(random_angle)
    else:
        robot.drive(-150, 0)

    wait(10)

    # Explorer
    # 1. The robot moves forward until it detects soomething then turns a random angle between -180 and 180 degrees and continues moving forward.
    # 2. The robot should calculate how far the object is, beep, then shortly afterwards turn a random angle and continue.
    # 3. It should continue driving.
    # 4. 200 mm
    """ 5. 
    Turn on.
    Enter the while loop.
    Continue driving forward.
    Detect an object within 200 mm.
    Calculate how far the object is.
    Beep.
    Turn a random angle between -180 and 180 degrees.
    Restart the while loop.
    """